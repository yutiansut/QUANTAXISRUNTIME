from stock_hq_pb2 import hq_struct
import pandas as pd


def parse_from_proto(data):
    mask=['datetime', 'last_close', 'code', 'open', 'high', 'low', 'price', 'cur_vol',
                       's_vol', 'b_vol','volume', 'ask1', 'ask_vol1', 'bid1', 'bid_vol1', 'ask2', 'ask_vol2',
                       'bid2', 'bid_vol2', 'ask3', 'ask_vol3', 'bid3', 'bid_vol3', 'ask4',
                       'ask_vol4', 'bid4', 'bid_vol4', 'ask5', 'ask_vol5', 'bid5', 'bid_vol5']
    if isinstance(data,list):
        return pd.DataFrame([[_.datetime,_.last_close,_.code,_.open,_.high,_.low,_.price,_.cur_vol,_.s_vol,
                              _.b_vol,_.volume,_.ask1,_.ask_vol1,_.bid1,_.bid_vol1,_.ask2,_.ask_vol2,_.bid2,_.bid_vol2,
                              _.ask3,_.ask_vol3,_.bid3,_.bid_vol3, _.ask4,_.ask_vol4,_.bid4,_.bid_vol4, 
                              _.ask5,_.ask_vol5,_.bid5,_.bid_vol5 ] for _ in data],columns=mask)
    else:
        return parse_from_proto([data])
            
            




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


