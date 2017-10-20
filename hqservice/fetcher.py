from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import wait, as_completed
from pytdx.hq import TdxHq_API
from stock_min_pb2 import stock_min
def __select_market_code(code):
    code = str(code)
    if code[0] in ['5', '6', '9'] or code[:3] in ["009", "126", "110", "201", "202", "203", "204"]:
        return 1
    return 0


def change(pack,code):
    data=stock_min()
    data.open=pack[0]['open']
    data.close=pack[0]['close']
    data.high=pack[0]['high']
    data.low=pack[0]['low']
    data.code=str(code)[0:6]
    data.volume=pack[0]['vol']
    
    return data


def task(code, timeout=100):
    api = TdxHq_API()
    api.connect('115.238.90.165', 7709)
    market = __select_market_code(code)
    res = api.get_security_bars(1, market, code, 0,1)
    #re=[change(x,code) for x in res]
    #res=api.get_security_quotes([(__select_market_code(code), code)])
    return change(res,code)




def QA_Fetcher(code,type_):
    with Pool(max_workers=40) as executor:
        future_tasks = [executor.submit(task, code,type_)]
        for f in future_tasks:
            if f.running():
                print('%s is running' % str(f))
        for f in as_completed(future_tasks):
            try:
                if f.done():
                    data=f.result()
                    return data
            except Exception as e:
                f.cancel()
                print(str(e))

