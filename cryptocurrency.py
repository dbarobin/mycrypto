#!/usr/bin/python
# coding:utf8
'''
@time     : 2017/12/12 12:48
@author   : Robin Wen
@site     : dbarobin.com
@file     : cryptocurrency.py
@desc     : Count my cryptocurrency.
@project  : BlockchainAge
@software : PyCharm Pro
@ref      : https://coinmarketcap.com/api
@version  : v1.0
'''

# Import related class.
import requests
import json

'''
Coinmarketcap requests.

Args:
    ticker: cryptocurrency symbol.
    convert: which currency to convert.

Returns:
    req: coinmarketcap requests.
'''
def Coinmarketcap(ticker, convert):
    url = ('https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s') \
    % (ticker, convert)
    req = requests.get(url)
    return req

'''
Count my cryptocurrency.

Args:
    file: cryptocurrency file.
    cryptocurrency.txt includes my cryptocurrency detail.
    This file seperated by one space.
    First column: tikcker id.
    Second column: ticker nums.

Returns:
    price_all: All cryptocurrency convert to CNY.
'''
def CountCryptoCurrency(file):
    # counter.
    price_all = 0
    for line in open(file):
        columns = line.split(' ')
        ticker = columns[0]
        nums = columns[1]
        req = Coinmarketcap(ticker, 'CNY')
        for item in req.json():
            price_cny = item['price_cny']
            price_total = float(price_cny) * float(nums)
            price_all = float(price_all) + float(price_total)

    return price_all

# Main function.
if __name__ == "__main__":
    price_all = CountCryptoCurrency('cryptocurrency.txt')
    print ("Your cryptocurrency value: ¥%s") % (price_all)
