
from __future__ import print_function

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc


def run():
  channel = grpc.insecure_channel('localhost:50052')
  stub = stock_hq_pb2_grpc.StockHQServiceStub(channel)
  response = stub.QA_fetch_get(stock_hq_pb2.Query(code='601801',type='1min'))
  print([response.code,response.open,response.high,response.low,response.close])


if __name__ == '__main__':
  run()
