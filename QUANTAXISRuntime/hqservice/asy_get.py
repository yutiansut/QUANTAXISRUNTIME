
import queue
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from pytdx.hq import TdxHq_API
import asyncio




class ConcurrentApi:
    def __init__(self, *args, **kwargs):
        self.thread_num = kwargs.pop('thread_num', 4)
        self.ip = kwargs.pop('ip', '14.17.75.71')
        self.executor = ThreadPoolExecutor(self.thread_num)

        self.queue = queue.Queue(self.thread_num)
        for i in range(self.thread_num):
            api = TdxHq_API(args, kwargs)
            api.connect(self.ip)
            self.queue.put(api)

    def __getattr__(self, item):
        api = self.queue.get()
        func = api.__getattribute__(item)

        def wrapper(*args, **kwargs):
            res = self.executor.submit(func,*args, **kwargs)
            self.queue.put(api)
            return res
        return wrapper


def get_market(code):
    code = str(code)
    if code[0] in ['5', '6', '9'] or code[:3] in ["009", "126", "110", "201", "202", "203", "204"]:
        return 1
    return 0
# 获取股票列表，并行版
def concurrent_api(num=4):
    capi = ConcurrentApi(thread_num=num)
    now = datetime.now()
    data = {capi.get_security_list(0, 100) for i in range(100)}
    dd = [i.result() for i in data]
    return (datetime.now() - now).total_seconds()


# 获取股票列表，原生版
def original_api():
    api = TdxHq_API()
    api.connect()
    now = datetime.now()
    dd = [api.get_security_list(0, 100) for i in range(100)]
    return (datetime.now() - now).total_seconds()

import tushare as ts
code=ts.get_stock_basics().index.tolist()
best_ip='115.238.90.165'


#获取全市场行情，并行版
def concurrent_quotes(num=20):
    capi = ConcurrentApi(thread_num=num, ip=best_ip)
    now = datetime.now()
    data = {capi.get_security_quotes([(get_market(x), x) for x in code[80 * pos:80 * (pos + 1)]]) for pos in range(int(len(code) / 80) + 1)}
    #print(data)
    dd = [i.result() for i in data]
    print((datetime.now() - now).total_seconds())
    return dd


#获取全市场行情，原生版
def original_quotes():
    api = TdxHq_API()
    api.connect(best_ip)
    now = datetime.now()
    data = [api.get_security_quotes(
        code[80 * pos:80 * (pos + 1)]) for pos in range(int(len(code) / 80) + 1)]
    return (datetime.now() - now).total_seconds()




a=concurrent_quotes()
print(len(a))