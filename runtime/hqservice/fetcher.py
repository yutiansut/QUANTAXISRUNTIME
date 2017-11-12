from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import wait, as_completed
from pytdx.hq import TdxHq_API
from stock_hq_pb2 import hq_struct
from runtime.fetcher.fetch import QA_Tdx_Executor

def __select_market_code(code):
    code = str(code)
    if code[0] in ['5', '6', '9'] or code[:3] in ["009", "126", "110", "201", "202", "203", "204"]:
        return 1
    return 0



def changer(pack, code):
    #print(pack)
    data = hq_struct()
    data.open = pack['open']
    data.close = pack['close']
    data.high = pack['high']
    data.low = pack['low']
    data.code = str(code)[0:6]
    data.volume = pack['vol']
    data.datetime= pack['datetime']

    return data

def single_task(code, timeout=100):
    api = TdxHq_API()
    api.connect('115.238.90.165', 7709)
    market = __select_market_code(code)
    res = api.get_security_bars(1, market, code, 0, 1)[0]
    #re=[change(x,code) for x in res]
    #res=api.get_security_quotes([(__select_market_code(code), code)])
    return changer(res, code)
def multiple_task(code, timeout=100):
    api = TdxHq_API()
    api.connect('115.238.90.165', 7709)
    market = __select_market_code(code)
    res = api.get_security_bars(1, market, code, 0, 800)
    
    re=[changer(x,code) for x in res]
    #print(re)
    #res=api.get_security_quotes([(__select_market_code(code), code)])
    return re

def QA_Fetcher(code, type_):
    with Pool(max_workers=40) as executor:
        future_tasks = [executor.submit(single_task, code, type_)]
        for f in future_tasks:
            if f.running():
                print('%s is running' % str(f))
        for f in as_completed(future_tasks):
            try:
                if f.done():
                    data = f.result()
                    return data
            except Exception as e:
                f.cancel()
                print(str(e))

def QA_Fetcher_long(code, type_):
    with Pool(max_workers=40) as executor:
        future_tasks = [executor.submit(multiple_task, code, type_)]
        for f in future_tasks:
            if f.running():
                print('%s is running' % str(f))
        for f in as_completed(future_tasks):
            try:
                if f.done():
                    data = f.result()
                    print(data[-2])
                    return data
            except Exception as e:
                f.cancel()
                print(str(e))

def QA_fetch_all_market(code):
    executor=QA_Tdx_Executor(thread_num=4)
    return executor.get_realtime_concurrent(code)


if __name__ =='__main__':
    #QA_Fetcher_long('000001','9')
    print(QA_fetch_all_market('000001'))