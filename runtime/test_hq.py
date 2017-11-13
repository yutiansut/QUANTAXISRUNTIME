from hqservice.fetcher import quotation


import QUANTAXIS as QA
stock_list=QA.QA_fetch_stock_block_adv().code


for i in range(100):
    print(len(quotation(stock_list)))