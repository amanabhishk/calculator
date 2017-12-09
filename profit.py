import numpy as np
import sys
BTC, LTC, ETH  = dict(), dict(), dict()

BTC["Nov26"] = [100,97.01,9212.64]
BTC["Dec07"] = [400,394.13,15218.40]

LTC["Dec07"] = [100,97.01,98.98]

ETH["Dec07"] = [100,97.01,431.65]

def gain(d,PRICE):
    PRICE = float(PRICE)
    spent, gained = list(), list()
    for index, key in enumerate(d):
        x = d[key][0]
        spent.append(x)
        y = (d[key][1]/d[key][2])*PRICE
        gained.append(y)
        print("{0} {1:.0f} {2:.0f} {3:+.0f}".format(key,x,y,y-x))
    print("Total {0:.0f} {1:.0f} {2:+.0f}".format(sum(spent),sum(gained),sum(gained)-sum(spent)))
    return np.array(spent), np.array(gained), np.array(gained)-np.array(spent)

if __name__=="__main__":
    if len(sys.argv) != 4:
        print("$python profit.py BTC_price ETH_price LTC_price")
    else:
        print("\n\nBTC:")
        BTC_= gain(BTC,sys.argv[1])
        print("\nETH:")
        ETH_ = gain(ETH,sys.argv[2])
        print("\nLTC:")
        LTC_ = gain(LTC,sys.argv[3])

        print("--------")
        x = BTC_[0].sum()+LTC_[0].sum()+ETH_[0].sum()
        y = BTC_[1].sum()+LTC_[1].sum()+ETH_[1].sum()
        print("Total {0:.0f} {1:.0f} {2:+.0f}".format(x,y,y-x))
        print("\n")

