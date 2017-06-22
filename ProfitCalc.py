import urllib2
import json
from Tkinter import *
import tkMessageBox
import os
import time
from decimal import *
import tkFont
import ConfigParser

#IF UseConfig is 1, then settings above will be ignored
#Set it to 0, if u want single-exe
UseConfig = 1

urlToPool = ""
PoolName = ""
CurrencyShortName = ""
CoinMarketCapCurrencyName = ""
AvailableBlocksInStats = 0


Config = ConfigParser.ConfigParser()
Config.read("config.txt")

if (UseConfig == 1):
    page = Config.get("Main", 'urlToPool')
    poolname = Config.get("Main", 'PoolName')
    cshortname = Config.get("Main", 'CurrencyShortName')
    cmcname = Config.get("Main", 'CoinMarketCapCurrencyName')
    aabks = int(Config.get("Main", 'AvailableBlocksInStats'))
else:
    page = urlToPool
    poolname = PoolName
    cshortname = CurrencyShortName
    cmcname = CoinMarketCapCurrencyName
    aabks = int(AvailableBlocksInStats)
    

api = ""
url = ""
urla = ""
result = 0
sresult = ""


def calc():
    url = page + "index.php?page=api&action=getblocksfound&api_key="
    urla = page + "index.php?page=api&action=getusertransactions&api_key="
    blockno = (aabks - 2)
    blocktime = 0
    api = e1.get()
    blocks = urllib2.urlopen(url + api).read()

    block = json.loads(blocks)

    block = block['getblocksfound']['data']
    while (blockno != 0):
        blocktime = blocktime + (block[blockno]['time'] - block[(blockno + 1)]['time'])
#        print(blocktime)
        blockno = blockno - 1
    blocktime = blocktime / (aabks - 2)


    trans = urllib2.urlopen(urla + api).read()
    tran = json.loads(trans)
    tran = tran['getusertransactions']['data']['transactions']
    a = aabks
    b = 0
    tranmoney = 0
    tranmoney = float(tranmoney)

    while(a != 0):
        if (tran[a]['type'] == "Credit"):

            b = b + 1
            tranmoney = tranmoney + float(tran[a]['amount'])
#            print(tranmoney)
            a = a - 1
        else:
            a = a - 1
    avge = 0
    avge = float(avge)
    avge = float((tranmoney / b))
    result = float((avge / (blocktime / 60)) * 60)
#    print(avge)
#    print(blocktime)
    result = result - ((result / 100) * 1.337)
    sresult = str(result)
    prices = urllib2.urlopen("https://api.coinmarketcap.com/v1/ticker/" + cmcname).read()
    pricea = json.loads(prices)
#    tkMessageBox.showinfo("Done!", "Your hourly profit is: " + str(result) + " VRM and daily: " + str(result * 24) + " VRM")
    l6 = Label(f1, text=round(result, 8))
    l6.pack(side = RIGHT)
    l8 = Label(f2, text=round((result * 24), 8))
    l8.pack(side = RIGHT)
    btcp = pricea[0]['price_btc']
    btcp = float(btcp)
    usdp = pricea[0]['price_usd']
    usdp = float(usdp)
    up = (usdp * result)
    hvb = (btcp * result)
    l10 = Label(f3, text=format(hvb, '.8f'))
    l10.pack(side = RIGHT)
    l11 = Label(f4, text=format((hvb * 24), '.8f'))
    l11.pack(side=RIGHT)
    l10a = Label(f3a, text=format(up, '.2f'))
    l10a.pack(side = RIGHT)
    l11a = Label(f4a, text=format((up * 24), '.2f'))
    l11a.pack(side=RIGHT) 
a = Tk()
a.wm_title(poolname + " Profit Calc")
l1 = Label(a, text="Welcome to the " + cshortname +  " Profit Calculator.", pady=15)
l1.config(font=('Helvetica 12 bold'))
l1.pack()
l2 = Label(a, text="Please don't look at the source code it is not cleaned up!")
l2.pack()
l3 = Label(a, text="Made by Marekkon5, Version: 2")
l3.pack()
l4 = Label(a, text=poolname + " API Key: ")
l4.pack()
e1 = Entry(a, width=64)
e1.pack()
b1 = Button(a, text="Calculate!", command = calc)
b1.pack()
f1 = Frame(a)
f1.pack()
l5 = Label(f1, text="Hourly Profit (" + cshortname + "): ", fg='magenta')
l5.pack(side = LEFT)
f2 = Frame(a)
f2.pack()
l7 = Label(f2, text="Daily Profit ("  + cshortname + "): ", fg='magenta')
l7.pack(side = LEFT)
f3 = Frame(a)
f3.pack()
l9 = Label(f3, text="Hourly Profit (BTC):", fg='red')
l9.pack(side = LEFT)
f4 = Frame(a)
f4.pack()
f3a = Frame(a)
f3a.pack()
l11 = Label(f4, text="Daily Profit (BTC):", fg='red')
l11.pack(side = LEFT)
l9a = Label(f3a, text="Hourly Profit (USD):", fg='blue')
l9a.pack(side = LEFT)
f4a = Frame(a)
f4a.pack()
l11a = Label(f4a, text="Daily Profit (USD):", fg='blue')
l11a.pack(side = LEFT)
l15 = Label(a, text="Prices source: coinmarketcap.com")
l15.config(font=('Helvetica 8 italic'))
l15.pack()
l16 = Label(a, text="Source & Info: github.com/Marekkon5/MPOSProfitCalc")
l16.config(font=('Helvetica 8 italic'))
l16.pack()
a.mainloop()
