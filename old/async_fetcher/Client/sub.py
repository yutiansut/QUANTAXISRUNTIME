import asyncio
import aiozmq.rpc
from itertools import count




""""
sub是服务端 函数运行在sub上 pub可以在另外一个进程里面调用sub的函数

"""
class Handler(aiozmq.rpc.AttrHandler):

    def __init__(self):
        self.connected = False
        self.data=[]
    @aiozmq.rpc.method
    def remote_func(self, step, a: int, b: int):
        self.connected = True
        self.data=[1,2,34,5,66,3432,213,23,12]
        print('sub')
        print("HANDLER", step, a, b)


@asyncio.coroutine
def go():
    handler = Handler()
    subscriber = yield from aiozmq.rpc.serve_pubsub(
        handler, subscribe='topic', bind='tcp://127.0.0.1:12345',
        log_exceptions=True)
    print(subscriber)
    #subscriber.close()
    for step in count(0):
        print(handler.connected)

        print(handler.data)
        if handler.connected:
                break
        else:
            yield from asyncio.sleep(0.3)

        #print(handler.connected)
    #yield from subscriber.wait_closed()

asyncio.get_event_loop().run_until_complete(go())