from hqservice.singleclient import QA_Runtime_single_client
import QUANTAXIS as QA
import threading
class sc(QA_Runtime_single_client):
    


    def OnReqDepthMarketData(self,data):
        print(len(data))
    def OnSubscribe(self,data):
        try:
            print(len(data[0]))
        except:
            pass
stock_list=QA.QA_fetch_stock_block_adv().code
print(1)
c=sc()
c.connect()
c.Subscribe(stock_list[0:500])
    #print(c._quotation_(stock_list[0:500]))
    #print(threading.enumerate())

print(c._sub_code)