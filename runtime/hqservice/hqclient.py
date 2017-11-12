
from __future__ import print_function

import asyncio
import concurrent
import datetime
import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Timer

import grpc
from aiogrpc import insecure_channel

import stock_hq_pb2
import stock_hq_pb2_grpc
import pandas as pd
from parser_proto import parse_from_proto
"""
有四种通信模式:


1.点对点p2p
2.点对流p2s
3.流对点s2p
4.流对流s2s

"""
stock_list = ['000001', '000002', '000004', '600010']


def gen():
    for item in stock_list:
        yield stock_hq_pb2.query_struct(code=item, type='1min')


def quo_gen():
    # while datetime.datetime.now()

    for i in range(100000):
        yield stock_hq_pb2.query_realtime(code=' '.join(stock_list))


class req_job():
    def __init__(self, func, callback_func, *args, **kwargs):
        self.func = func
        self.callback = callback_func
        self.res = None


class QA_Runtime_client:
    def __init__(self, broker='192.168.4.239:50052', *args, **kwargs):

        self.broker = broker
        self.channel = grpc.insecure_channel(self.broker)
        self.async_channel = insecure_channel(self.broker)
        self._event_thread = Thread(target=self.event_notify, name='EVENT')
        self._callback_thread = Thread(target=self.callback, name='CALLBACK')
        self._quotation_thread = Thread(
            target=self.quotation, name='Quotation')
        self._callback_thread_alive = True
        self._quotation_thread_alive = True
        self._callback_queue = queue.Queue()
        self._event_loop = asyncio.get_event_loop()
        self._sub_code = []
        self._res = queue.Queue(maxsize=100)

    def _generator(self, stock_list, type_list):

        type_list = type_list if isinstance(type_list, list) else [type_list]
        stock_list = stock_list if isinstance(
            stock_list, list) else [stock_list]

        for item in type_list:
            for code in stock_list:
                yield stock_hq_pb2.query_struct(code=code, type=item)

    def _quotation(self, code):
        return [_ for _ in self.stub.QA_fetch_realtime(stock_hq_pb2.query_realtime(code=' '.join(code)))]

    def connect(self):

        self.stub = stock_hq_pb2_grpc.StockHQServiceStub(self.channel)
        self.async_stub = stock_hq_pb2_grpc.StockHQServiceStub(
            self.async_channel)
        self._callback_thread.start()
        # self._event_thread.start()
        self._quotation_thread.start()

    def event_notify(self):
        try:
            self._event_loop.run_forever()
        finally:
            self._event_loop.stop()

    def callback(self):
        while self._callback_thread_alive:
            while self._callback_queue.qsize() > 0:
                _job = self._callback_queue.get()
                try:
                    _job.res = eval(_job.func)
                    if _job.res is not None:
                        self._res.put_nowait(_job.res)

                        eval(_job.callback)
                    else:
                        self._res.put(None)

                        # Timer(_job['last_gap'],self._callback_queue.put(_job)).start()
                except Exception as e:
                    raise e

    def p2p(self):
        response = self.stub.QA_fetch_p2p(
            stock_hq_pb2.query_struct(code='601801', type='1min'))
        print(response.code, response.open,
              response.high, response.low, response.close)

    def p2s(self):
        resp = self.stub.QA_fetch_p2s(
            stock_hq_pb2.query_struct(code='601801', type='1min'))
        print([(response.code, response.open, response.high,
                response.low, response.close) for response in resp])

    def s2s(self):
        resp = self.stub.QA_fetch_s2s(gen())
        print([(response.code, response.open, response.high,
                response.low, response.close, response.datetime) for response in resp])

    def quotation(self):
        while self._quotation_thread_alive:

            self._sub_code = list(set(self._sub_code))
            if len(self._sub_code) > 0:
                _data = self._quotation(self._sub_code)
                self.OnSubscribe([_x for _x in _data])
            else:
                pass
            time.sleep(1)

    async def asyReqDepthMarketData(self, code):

        return await self.async_stub.QA_fetch_realtime(stock_hq_pb2.query_realtime(code=' '.join(code)))

    def ReqDepMarketData(self, code):
        _job = req_job('self._quotation({})'.format(
            code), 'self.OnReqDepthMarketData()')
        self._callback_queue.put(_job)

    def OnReqDepthMarketData(self):
        data = self._res.get()
        if data is not None:
            #print(data[0])
            print(parse_from_proto(data))
            #print(pd.DataFrame([data[0]]))

    # 订阅(直到结束)
    def Subscribe(self, code=stock_list):

        print('SUB {}'.format(code))
        self._sub_code.extend(code)

    def OnSubscribe(self, data):
        # data=self._res.get()
        if data is not None:
            print('CALLBACK')
            print(parse_from_proto(data))
        else:
            print('wrong')

    def Unsubscribe(self, code):
        print('UNSUB {}'.format(code))
        self._sub_code = list(set(self._sub_code).difference(set(code)))
        print(self._sub_code)

    def _subscribe(self, code):
        asyncio.run_coroutine_threadsafe(
            self.ReqDepthMarketData(code), self._event_loop)

    def disconnect(self):
        pass


if __name__ == '__main__':

    client = QA_Runtime_client(broker='192.168.4.239:50052')
    client.connect()
    #print(threading.enumerate())
    # client.Subscribe()
    client.Subscribe(stock_list)
    time.sleep(3)
    client.Unsubscribe(['000001'])
    client.ReqDepMarketData(['000001'])
    # client.subscribe()
    # time.sleep(2)
    client.disconnect()
    # print('close')
