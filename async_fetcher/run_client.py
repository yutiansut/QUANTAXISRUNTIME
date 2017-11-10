# coding:utf-8


import socket
import asyncio
import threading
from threading import Thread



class Client():
    def __init__(self, *args, **kwargs):
        self._thread_manager=[]
        self._loop = asyncio.get_event_loop()
        self._web_loop=asyncio.get_event_loop()
        self._s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self._s1.bind(('127.0.0.1',5129) )
        self._s1.listen(10000)
        self.connection, self.address = self._s1.accept()




    def start_loop(self,loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()

    def demon(self):
        
        self._dem= Thread(target=self.start_loop, args=(self._web_loop,))
        self._dem.start()

    async def event_dispatcher(self,event):
        if event in ['web']:
            #self._web_loop.add_reader(self.connection,self.web_event)
            self.con=self._web_loop.create_connection('127.0.0.1',5214)
            reader, writer = yield from self.con
    def web_event(self):
        data = self.connection.recv(100)
        if len(data)>0:
            print("Received:", data.decode())
        
    def start(self):
        self.demon()

        asyncio.run_coroutine_threadsafe(self.event_dispatcher('web'), self._web_loop)


if __name__=='__main__':
    c=Client()
    c.start()