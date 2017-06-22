## MPOS Pool Profit Calculator

### Created by Marekkon5

### Usage:

#### Edit config.txt to match your pool:

[Main]
1. urlToPool: **Pool URL, Ex: http://zec.suprnova.cc/**

2. PoolName: **Pool Name, Ex: ZEC Suprnova**

3. CurrencyShortName: **Currency Short Name, Ex: ZEC**

4. CoinMarketCapCurrencyName: **CoinMarketCap.com Currency Name, Ex: ZCash**

5. AvailableBlocksInStats: **Available Blocks In Pool Statistics, Ex: 20**

6. AvailableBlocksInStats - you can get this value from pool > statistics > blocks

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
#### IMPORTANT! The binary also requires config.txt!

RELEASES Also Available


### How it works:  

Simply avg block time and avg reward....  
...and some simple maths...  



Donate (BTC): 1GEPkNwzTdwuNbPAwYF5LnRfgMhS4g7mmi