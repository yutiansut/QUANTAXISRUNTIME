import motor
import asyncio
from motor import motor_asyncio
from motor.motor_asyncio import (AsyncIOMotorCollection,AsyncIOMotorClient,AsyncIOMotorDatabase,
                                 AsyncIOMotorCommandCursor)
import pymongo
import datetime
import tushare as ts

code_list=ts.get_zz500s().code.tolist()
time1=datetime.datetime.now()
client=AsyncIOMotorClient('127.0.0.1',27017).quantaxis.stock_day
print(client)

data=[]
print('async-mongo')
async def get_data(code,func,data,*args,**kwargs):
   #data=[]
    async for message in client.find({'code':code}):
        data.append(message)
        #print(message)
    return func(data,*args,**kwargs)




def callback(data):
    pass


loop=asyncio.get_event_loop()
event=[asyncio.ensure_future(get_data(code,callback,data)) for code in code_list]

loop.run_until_complete(asyncio.wait(event))
print(datetime.datetime.now()-time1)
print(len(data))
