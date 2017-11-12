#coding:utf-8

import asyncio
class QA_AsyncTasker():
    def __init__(self, *args, **kwargs):
        self._loop=asyncio.get_event_loop()
        self.eventer=[]
    def start(self):
        self._loop.run_forever()

    def add_job(self,await_job):
        self.eventer.append(asyncio.ensure_future(await_job))



import asyncio
import time
import threading
now = lambda: time.time()
from threading import Thread
from multiprocessing import Process
from multiprocessing import Manager

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
 
async def do_some_work(x):
    print('{} Waiting {}'.format(threading.current_thread(),x))
    await asyncio.sleep(x)
    print('{} Done after {}s'.format(threading.current_thread(),x))
 
def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))
 
start = now()
new_loop = asyncio.new_event_loop()
loop2=asyncio.new_event_loop()


t = Thread(target=start_loop, args=(new_loop,))

s = Thread(target=start_loop, args=(loop2,))
t.start()
s.start()

print('{} TIME: {}'.format(threading.current_thread(),time.time() - start))
 
asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), loop2)
asyncio.run_coroutine_threadsafe(do_some_work(6), loop2)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)

for i in range(21):
    print('{} CurrentTime {} '.format(threading.current_thread(),time.time()))
    time.sleep(0.5)
asyncio.run_coroutine_threadsafe(do_some_work(0.5), new_loop)