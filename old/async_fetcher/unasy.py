
import pymongo
import datetime
import tushare as ts
code_list=ts.get_zz500s().code.tolist()

print('unasync-mongo')
time2=datetime.datetime.now()
clientx=pymongo.MongoClient('192.168.4.253',27017).quantaxis.stock_day
data=[]
def get_data(codelist):
    for code in codelist:
        for message in clientx.find({'code':code}):
            data.append(message)


get_data(code_list)
print(datetime.datetime.now()-time2)