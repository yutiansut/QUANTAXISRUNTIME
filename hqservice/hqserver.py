from concurrent import futures
import time

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class StockHQService(stock_hq_pb2_grpc.StockHQServiceServicer):

  def SayHello(self, request, context):
    return stock_hq_pb2.Query(message='Hello, %s!' % request.code)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  stock_hq_pb2_grpc.add_StockHQServiceServicer_to_server(StockHQService(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  serve()
