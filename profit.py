import sys
BTC, LTC, ETH  = dict(), dict(), dict()

BTC["Nov26"] = [100,97.01,9212.64]
BTC["Dec07"] = [400,394.13,15218.40]

LTC["Dec07"] = [100,97.01,98.98]

ETH["Dec07"] = [100,97.01,431.65]

def gain(d,PRICE):
    PRICE = float(PRICE)
    spent, gained = 0, 0
    for index, key in enumerate(d):
        spent += d[key][0]
        gained += (d[key][1]/d[key][2])*PRICE
    return spent, gained, gained-spent


if __name__=="__main__":
    if len(sys.argv) != 4:
        print("$python profit.py BTC_price ETH_price LTC_price")
    else:
        print("BTC:")
        print(gain(BTC,sys.argv[1]))
        print("ETH")
        print(gain(ETH,sys.argv[2]))
        print("LTC:")
        print(gain(LTC,sys.argv[3]))


