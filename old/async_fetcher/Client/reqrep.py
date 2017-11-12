import asyncio
from aiozmq import rpc
from itertools import count
import datetime,time
class Handler(rpc.AttrHandler):

    @rpc.method
    def remote(self, arg1, arg2):
        for i in range(2):
            time.sleep(1)
            yield str(datetime.datetime.now())

    @rpc.method
    def remote2(self, arg1, arg2):
        for i in range(2):
            time.sleep(5)
            yield 'abc{}'.format(str(datetime.datetime.now()))
@asyncio.coroutine
def go():
    server =  yield from rpc.serve_rpc(Handler(),
                                       bind='tcp://127.0.0.1:5552')

    client = yield from rpc.connect_rpc(connect='tcp://127.0.0.1:5552')

    ret=yield from client.call.remote(1, 2)
    ta=yield from client.call.remote2(1,2)
    print(ret)
    print(ta)


asyncio.get_event_loop().run_until_complete(go())