
import asyncio
import time
import datetime
import threading
import aiozmq
import grpc
import aiozmq.rpc
from itertools import count
from threading import Thread
from library.high_level_protocol import AsyncMongo_Protocol

class Handler(aiozmq.rpc.AttrHandler):
    
    def __init__(self):
        self.connected = False

    @aiozmq.rpc.method
    def remote_func(self, step, a: int, b: int):
        self.connected = True
        print("HANDLER", step, a, b)

class Client():
    def __init__(self, *args, **kwargs):

        self.start_bat()

    def start_bat(self):
        # 按照阻塞的可能性 开线程

        self.backend_loop = asyncio.new_event_loop()
        self.backend = Thread(target=self.set_loop, args=(self.backend_loop,))
        self.backend.setName('Backend Event Server')
        self.backend.start()

        self.quotation_loop = asyncio.new_event_loop()
        self.quotation = Thread(target=self.set_loop,
                                args=(self.quotation_loop,))
        self.quotation.setName('Quotation Event Server')
        self.quotation.start()
    def run(self,*args,**kwargs):
        return asyncio.run_coroutine_threadsafe(*args,**kwargs)

    
    def set_loop(self, loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    async def do_some_work(self, func, timer):
        loop = asyncio.get_event_loop()
        await asyncio.sleep(timer)

        loop = asyncio.get_event_loop()
        print(loop)
        asyncio.run_coroutine_threadsafe(self.do_some_work(func, timer), loop)

    async def event_job(self, reader, writer):

        print('{} Waiting Requests on 8888'.format(asyncio.get_event_loop()))
        subscriber_addr='tcp://127.0.0.1:8889'
        publisher = await aiozmq.rpc.connect_pubsub(connect=subscriber_addr)
        handler = Handler()
        for step in count(0):
            await publisher.publish('topic').remote_func(step, 1, 2)

        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')
        print("Received %r from %r" % (message, addr))

        print("Send: %r" % message)
        writer.write(data)
        await writer.drain()
        #self._start_server()
        print("Close the client socket")
        writer.close()

    def start_server(self,protocol,port):
        self._start_server(protocol,8889)

    def _start_server(self,protocol=AsyncMongo_Protocol,port=8889):
        print('{} Waiting Requests on {}'.format(asyncio.get_event_loop(),port))
        coro2=self.backend_loop.create_server(AsyncMongo_Protocol, '127.0.0.1', port)
        self.run(coro2,self.backend_loop)
    
    
    def start(self):
        coro = asyncio.start_server(
            self.event_job, '127.0.0.1', 8888, loop=self.backend_loop)
        self.run(coro,self.backend_loop)
        #coro2=self.backend_loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8889)
        #self.run(coro2,self.backend_loop)


        # asyncio.run_coroutine_threadsafe(self.do_some_work(1,2),self.backend_loop)

        #asyncio.run_coroutine_threadsafe(
        #    self.do_some_work(1, 3), self.quotation_loop)



client = Client()
client.start()
#coro=client.backend_loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8889)
#client.run(coro,client.backend_loop)
