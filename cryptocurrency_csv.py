#!/usr/bin/python
# coding:utf8
'''
@time     : 2018/06/13 10:27
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
import csv
import sys

'''
Coinmarketcap requests.

Args:
    ticker: cryptocurrency symbol.
    convert: which currency to convert.

Returns:
    req: coinmarketcap requests.
'''
def Coinmarketcap(ticker, convert):
    url = ('https://api.coinmarketcap.com/v1/ticker/%s/?convert=%s') % (ticker, convert)
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

    with open(file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            ticker = row[0]
            nums = row[1]
            req = Coinmarketcap(ticker, 'CNY')
            for item in req.json():
                price_cny = item['price_cny']
                price_total = float(price_cny) * float(nums)
                sys.stdout.write('%s %s %s %s\n' % (ticker, price_cny, str(nums), price_total))
                price_all = float(price_all) + float(price_total)

    return price_all

# Main function.
if __name__ == "__main__":
    price_all = CountCryptoCurrency('cryptocurrency.csv')
    print ("Your cryptocurrency value: ¥%s") % (price_all)
