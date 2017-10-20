
from __future__ import print_function

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc

stock_list = ['000001', '000002', '000004', '600010']


def gen():
    for item in stock_list:
        yield stock_hq_pb2.Query(code=item, type='1min')


"""
有四种通信模式:


1.点对点
2.点对流
3.流对点
4.流对流

"""


def p2p():
    channel = grpc.insecure_channel('192.168.4.239:50052')
    stub = stock_hq_pb2_grpc.StockHQServiceStub(channel)
    response = stub.QA_fetch_get(
        stock_hq_pb2.Query(code='601801', type='1min'))
    print(response.code, response.open,
          response.high, response.low, response.close)


def p2s():
    channel = grpc.insecure_channel('192.168.4.239:50052')
    stub = stock_hq_pb2_grpc.StockHQServiceStub(channel)
    resp = stub.QA_fetch_conn(stock_hq_pb2.Query(code='601801', type='1min'))
    print([(response.code, response.open, response.high,
            response.low, response.close) for response in resp])


def s2s():
    channel = grpc.insecure_channel('192.168.4.239:50052')
    stub = stock_hq_pb2_grpc.StockHQServiceStub(channel)
    resp = stub.QA_fetch_multi(gen())
    #response = stub.QA_fetch_get(stock_hq_pb2.Query(code='601801',type='1min'))
    print([(response.code, response.open, response.high,
            response.low, response.close) for response in resp])


if __name__ == '__main__':
    p2p()
    p2s()
    s2s()
