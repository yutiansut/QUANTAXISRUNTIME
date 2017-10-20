
from __future__ import print_function

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc
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


class QA_Runtime_client:
    def __init__(self, *args, **kwargs):
        self.channel = grpc.insecure_channel('192.168.4.239:50052')
        self.stub = stock_hq_pb2_grpc.StockHQServiceStub(self.channel)

    def connect(self,channel):
        self.channel = grpc.insecure_channel(channel)
        self.stub = stock_hq_pb2_grpc.StockHQServiceStub(self.channel)

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
        #response = stub.QA_fetch_get(stock_hq_pb2.query_struct(code='601801',type='1min'))
        print([(response.code, response.open, response.high,
                response.low, response.close, response.datetime) for response in resp])

    def _generator(self,stock_list,type_list):
        for item in type_list:
            for code in stock_list:
                yield stock_hq_pb2.query_struct(code=code, type=item)

    def subscribe(self,code,type='1min'):
        pass
    def unsubscribe(self):
        pass

if __name__ == '__main__':
    QA_Runtime_client().s2s()
