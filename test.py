# coding:utf-8


# coding: utf-8
from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import wait, as_completed
from pytdx.hq import TdxHq_API
import tushare as ts
import asyncio
import datetime
from stock_min_pb2 import stock_min
def __select_market_code(code):
    code = str(code)
    if code[0] in ['5', '6', '9'] or code[:3] in ["009", "126", "110", "201", "202", "203", "204"]:
        return 1
    return 0


CODE = ts.get_hs300s()['code'].tolist()[0:2]

#@asyncio.coroutine
def change(pack,code):
    data=stock_min()
    data.open=pack['open']
    data.close=pack['close']
    data.high=pack['high']
    data.low=pack['low']
    data.code=str(code)[0:6]
    return data



# 任务包 task_module
def task(code, timeout=100):
    api = TdxHq_API()
    api.connect('115.238.90.165', 7709)
    market = __select_market_code(code)
    res = api.get_security_bars(1, market, code, 0, 2)
    re=[change(x,code) for x in res]
    #res=api.get_security_quotes([(__select_market_code(code), code)])
    return re





# working_queue
import datetime
a = datetime.datetime.now()
data = []
with Pool(max_workers=40) as executor:
    future_tasks = [executor.submit(task, code) for code in CODE]
    for f in future_tasks:
        if f.running():
            print('%s is running' % str(f))
    for f in as_completed(future_tasks):
        try:
            if f.done():

                data.extend(f.result())

        except Exception as e:
            f.cancel()
            print(str(e))




#api = TdxHq_API()
print(data)
print([type(data_) for data_ in data])
#dt=[change(x) for x in data]
print(datetime.datetime.now() - a)
#print(dt)


