## MPOS Pool Profit Calculator

### Created by Marekkon5

### Usage:

#### Edit config.txt to match your pool:

[Main]
urlToPool: **Pool URL, Ex: http://zec.suprnova.cc/**
PoolName: **Pool Name, Ex: ZEC Suprnova**
CurrencyShortName: **Currency Short Name, Ex: ZEC**
CoinMarketCapCurrencyName: **CoinMarketCap.com Currency Name, Ex: ZCash**
AvailableBlocksInStats: **Available Blocks In Pool Statistics, Ex: 20**

AvailableBlocksInStats - you can get this value from pool > statistics > blocks

#### Then open or build (if u want to have exe for non-python users)

Open and Enter pool Api Key
The API Key Can be optained from pool / My Account / Edit Account
After Click Calculate!

### Build Guide:

1. Install pyinstaller:
	pip install pyinstaller
	
2. Build:
	pyinstaller ProfitCalc.py --onefile
	
And you are done


RELEASES Also Available


### How it works:

Simply avg block time and avg reward....
...and some simple maths...



Donate (BTC): 1GEPkNwzTdwuNbPAwYF5LnRfgMhS4g7mmi