from hqservice.hqclient import QA_Runtime_client
import QUANTAXIS as QA
import time,datetime
from hqservice.parser_proto import parse_from_proto

stock_list=QA.QA_fetch_stock_block_adv().code
start_time=datetime.datetime.now()
class client(QA_Runtime_client):

    def OnReqDepthMarketData(self,data):
        print(parse_from_proto(data))

    def OnSubscribe(self,data):
        now_time=datetime.datetime.now()
        print(now_time-start_time)
        print(now_time)
        #print(parse_from_proto(data))




client = client(broker='192.168.4.239:50052')
client.connect()

client.Subscribe(stock_list[0:500])
time.sleep(3)
client.Unsubscribe(['000001'])
client.ReqDepMarketData(['000001'])

client.disconnect()

