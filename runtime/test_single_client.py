from hqservice.singleclient import QA_Runtime_single_client
import QUANTAXIS as QA
import threading


class sc(QA_Runtime_single_client):

    def OnReqHistoryBar(self, data):
        """hundan"""
        print(data)
        
    def OnReqDepthMarketData(self, data):
        print(data)

    def OnSubscribe(self, data,time):
        try:
            print(len(data[0]))
        except:
            pass


stock_list = QA.QA_fetch_stock_block_adv().code

c = sc()
c.connect()
c.ReqDepMarketData(['000001'])
c.ReqHistoryBar(stock_list[0:500],'15min',5)
#c.Subscribe(stock_list[0:500])

print(c._sub_code)
