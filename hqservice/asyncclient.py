from aiogrpc import insecure_channel
import asyncio

import stock_hq_pb2
import stock_hq_pb2_grpc

channel = insecure_channel('ipv4:///192.168.4.239:50052')
stub = stock_hq_pb2_grpc.StockHQServiceStub(channel)

async def test_call():
    return await stub.QA_fetch_get(
        stock_hq_pb2.Query(code='601801', type='1min'))


response=test_call()
print(response.code, response.open,
        response.high, response.low, response.close)


#
#async def test_call_stream():
#    async for v in mystub.my_stream_method(...):
 #       ...


