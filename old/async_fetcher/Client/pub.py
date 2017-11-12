import asyncio
import aiozmq.rpc
from itertools import count


class Handler(aiozmq.rpc.AttrHandler):

    def __init__(self):
        self.connected = False
        self.data=[]

    @aiozmq.rpc.method
    def remote_func(self, step, a: int, b: int):
        self.connected = True
        print('pub')
        self.data=[1,2,34,5,66,3432,213,23,12]
        print("HANDLER", step, a, b)


@asyncio.coroutine
def go():
    handler = Handler()

    #print(list(subscriber.transport.bindings()))
    #s#ubscriber_addr = list(subscriber.transport.bindings())[0]
    #print("SERVE", subscriber_addr)

    publisher = yield from aiozmq.rpc.connect_pubsub(
        connect='tcp://127.0.0.1:12345')
    print(publisher)
    for step in count(0):
        yield from publisher.publish('topic').remote_func(step, 1, 2)


asyncio.get_event_loop().run_until_complete(go())