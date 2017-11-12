from concurrent import futures
import time

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc
#import stock_min_pb2
from fetcher import QA_Fetcher,QA_Fetcher_long



_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class StockHQService(stock_hq_pb2_grpc.StockHQServiceServicer):

  def QA_fetch_p2p(self, request, context):
    return QA_Fetcher(request.code,request.type)
  def QA_fetch_p2s(self,request,context):
    for item in QA_Fetcher_long(request.code,request.type):
          yield item
  def QA_fetch_s2s(self,request,context):
    for req in request:    
      for item in QA_Fetcher_long(req.code,req.type):
          yield item        


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  stock_hq_pb2_grpc.add_StockHQServiceServicer_to_server(StockHQService(), server)
  server.add_insecure_port('[::]:50052')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
