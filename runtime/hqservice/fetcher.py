# coding:utf-8
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import as_completed, wait

from pytdx.hq import TdxHq_API
from QUANTAXIS.QAFetch.QATdx_adv import QA_Tdx_Executor
import datetime
from stock_hq_pb2 import hq_struct


def __select_market_code(code):
    code = str(code)
    if code[0] in ['5', '6', '9'] or code[:3] in ["009", "126", "110", "201", "202", "203", "204"]:
        return 1
    return 0


def changer(pack, code):
    # print(pack)
    data = hq_struct()
    data.open = pack['open']
    data.close = pack['close']
    data.high = pack['high']
    data.low = pack['low']
    data.code = str(code)[0:6]
    data.volume = pack['vol']
    data.datetime = pack['datetime']

    return data

def _base_realtime_changer(_data,_time):
    data = hq_struct()
    data.last_close = float(_data['last_close'])
    data.open = float(_data['open'])
    data.price = float(_data['price'])
    data.high = float(_data['high'])
    data.low = float(_data['low'])
    data.code = str(_data['code'])
    data.cur_vol = float(_data['cur_vol'])
    data.b_vol = float(_data['b_vol'])
    data.s_vol = float(_data['s_vol'])
    data.volume = float(_data['vol'])
    data.ask1 = float(_data['ask1'])
    data.ask_vol1 = float(_data['ask_vol1'])
    data.ask2 = float(_data['ask2'])
    data.ask_vol2 = float(_data['ask_vol2'])
    data.ask3 = float(_data['ask3'])
    data.ask_vol3 = float(_data['ask_vol3'])
    data.ask4 = float(_data['ask4'])
    data.ask_vol4 = float(_data['ask_vol4'])
    data.ask5 = float(_data['ask5'])
    data.ask_vol5 = float(_data['ask_vol5'])
    data.bid1 = float(_data['bid1'])
    data.bid_vol1 = float(_data['bid_vol1'])
    data.bid2 = float(_data['bid2'])
    data.bid_vol2 = float(_data['bid_vol2'])
    data.bid3 = float(_data['bid3'])
    data.bid_vol3 = float(_data['bid_vol3'])
    data.bid4 = float(_data['bid4'])
    data.bid_vol4 = float(_data['bid_vol4'])
    data.bid5 = float(_data['bid5'])
    data.bid_vol5 = float(_data['bid_vol5'])
    data.datetime = str(_time)
    return data
def changer_realtime(pack, _time=datetime.datetime.now()):
    try:
        #print(len(pack))

        return [_base_realtime_changer(_data,_time) for item in pack for _data in item ]

    except Exception as e:
        pass


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

    re = [changer(x, code) for x in res]
    # print(re)
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


def quotation(code):
    executor = QA_Tdx_Executor(thread_num=4)
    _data,_time=executor.get_realtime_concurrent(code)
    return changer_realtime(_data,_time)

if __name__ == '__main__':
    # print(QA_Fetcher_long('000001','9'))
    print(quotation(['000001','000002']))
