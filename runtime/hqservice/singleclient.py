
from __future__ import print_function

import asyncio
import concurrent
import datetime
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Timer

import grpc
import pandas as pd
from aiogrpc import insecure_channel

from . import stock_hq_pb2, stock_hq_pb2_grpc
from .parser_proto import parse_from_proto
from .fetcher import _quotation as q
from .fetcher import _query_k as qk
"""
有四种通信模式:


1.点对点p2p
2.点对流p2s
3.流对点s2p
4.流对流s2s

"""
stock_list = ['000001', '000002', '000004', '600010']



class req_job():
    def __init__(self, func, callback_func, *args, **kwargs):
        self.func = func
        self.callback = callback_func
        self.res = None


class QA_Runtime_single_client:
    def __init__(self, *args, **kwargs):

        self._callback_thread = Thread(target=self.callback, name='CALLBACK',daemon=True)
        self._quotation_thread = Thread(
            target=self.quotation, name='Quotation')
        self._callback_thread_alive = True
        self._quotation_thread_alive = True
        self._callback_queue = queue.Queue()
        self._sub_code = []
        self._res = queue.Queue(maxsize=100)

    def _req_history_bar(self,code,_type,lens):
        data=qk(code,_type,lens)
        return data

    def _quotation_(self, code):
        _t=datetime.datetime.now()
        data,time=q(code)
        return data,time

    def connect(self):

        self._callback_thread.start()

        self._quotation_thread.start()

    def callback(self):
        for i in range(100000):
            if self._callback_queue.qsize() > 0:
                _job = self._callback_queue.get()
                try:
                    #print(_job.func)
                    _job.res = eval(_job.func)
                    if _job.res is not None:
                        self._res.put_nowait(_job.res)

                        eval(_job.callback)
                    else:
                        self._res.put(None)
                except Exception as e:
                    raise e
        time.sleep(1)

    def quotation(self):
        
        for i in range(100000):

            self._sub_code = list(set(self._sub_code))

            if len(self._sub_code) > 0:

                #print('before_q{}'.format(datetime.datetime.now()))
                _data,_time = self._quotation_(self._sub_code)
                #print('after_q{}'.format(datetime.datetime.now()))
                if _data is not None:
                    self.OnSubscribe(_data,_time)
                    #print('after_callback{}'.format(datetime.datetime.now()))
                
            else:
                pass

            time.sleep(2)


    def ReqDepMarketData(self, code):
        _job = req_job('self._quotation_({})'.format(
            code), 'self._OnReqDepthMarketData()')
        self._callback_queue.put(_job)

    def _OnReqDepthMarketData(self):
        data = self._res.get()
        if data is not None:
            self.OnReqDepthMarketData(data)

    def OnReqDepthMarketData(self,data):

        if data is None:
            raise Exception
    # 订阅(直到结束)

    def ReqHistoryBar(self, code,_type,lens):
        _job = req_job('self._req_history_bar({},\'{}\',{})'.format(
            code,str(_type),lens), 'self._OnReqHistoryBar()')
        self._callback_queue.put(_job)

    def _OnReqHistoryBar(self):
        data = self._res.get()
        if data is not None:
            self.OnReqHistoryBar(data)

    def OnReqHistoryBar(self,data):

        if data is None:
            raise Exception
    # 订阅(直到结束)






    def Subscribe(self, code=stock_list):
        self._sub_code.extend(code)
        
        #self.OnSubscribe(self._quotation_(self._sub_code)[0])
        

    def OnSubscribe(self, data,time):
        # data=self._res.get()
        if data is not None:
            print('CALLBACK')
            print(parse_from_proto(data))
        else:
            print('wrong')

    def Unsubscribe(self, code):
        #print('UNSUB {}'.format(code))
        self._sub_code = list(set(self._sub_code).difference(set(code)))
        #print(self._sub_code)


    def disconnect(self):
        pass


if __name__ == '__main__':

    client = QA_Runtime_single_client()
    client.connect()
    # print(threading.enumerate())
    # client.Subscribe()
    client.Subscribe(stock_list)
    #time.sleep(3)
    client.Unsubscribe(['000001'])
    client.ReqDepMarketData(['000001'])
    # client.subscribe()
    # time.sleep(2)
    client.disconnect()
    # print('close')
