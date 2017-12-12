import requests
import numpy as np
import sys
import csv

BTC, LTC, ETH  = dict(), dict(), dict()

with open('transactions.txt') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        if rows[0] == "BTC":
            BTC[rows[1]] = rows[2:]
        if rows[0] == "ETH":
            ETH[rows[1]] = rows[2:]
        if rows[0] == "LTC":
            LTC[rows[1]] = rows[2:]

def gain(d,PRICE):
    PRICE = float(PRICE)
    spent, gained = list(), list()
    for index, key in enumerate(d):
        x = float(d[key][0])
        spent.append(x)
        y = (float(d[key][1])/float(d[key][2]))*PRICE
        gained.append(y)
        print("{0} {1:.0f} {2:.0f} {3:+.0f}".format(key,x,y,y-x))
    print("Total {0:.0f} {1:.0f} {2:+.0f}".format(sum(spent),sum(gained),sum(gained)-sum(spent)))
    return np.array(spent), np.array(gained), np.array(gained)-np.array(spent)

if __name__=="__main__":
    url = 'https://api.coinbase.com/v2/prices/USD/spot?' 
    response = requests.get(url).json()
    print("\n\nBTC:")
    BTC_= gain(BTC,response["data"][0]["amount"])
    print("\nETH:")
    ETH_ = gain(ETH,response["data"][1]["amount"])
    print("\nLTC:")
    LTC_ = gain(LTC,response["data"][2]["amount"])

    print("--------")
    x = BTC_[0].sum()+LTC_[0].sum()+ETH_[0].sum()
    y = BTC_[1].sum()+LTC_[1].sum()+ETH_[1].sum()
    print("Total {0:.0f} {1:.0f} {2:+.0f}".format(x,y,y-x))
    print("\n")

