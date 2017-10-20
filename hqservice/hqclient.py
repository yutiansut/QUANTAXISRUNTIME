
from __future__ import print_function

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc

stock_list=['000001','000002','000004','600010']


def gen():
    for item in stock_list:
        yield stock_hq_pb2.Query(code=item,type='1min')


def run():
  channel = grpc.insecure_channel('localhost:50052')
  for i in gen():
      print(i)
  stub = stock_hq_pb2_grpc.StockHQServiceStub(channel)
  resp = stub.QA_fetch_multi(gen())
  #response = stub.QA_fetch_get(stock_hq_pb2.Query(code='601801',type='1min'))
  print([(response.code,response.open,response.high,response.low,response.close) for response in resp])


if __name__ == '__main__':
  run()
