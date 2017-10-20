from concurrent import futures
import time

import grpc

import stock_hq_pb2
import stock_hq_pb2_grpc
import stock_min_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class StockHQService(stock_hq_pb2_grpc.StockHQServiceServicer):

  def QA_fetch_get(self, request, context):
    #print(request.code)
    return stock_min_pb2.stock_min(code=request.code)


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
