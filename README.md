## MPOS Pool Profit Calculator

### Created by Marekkon5

![alt text](https://raw.githubusercontent.com/Marekkon5/MPOSProfitCalc/master/Screenshot1.png)

##### Requires Python 2 to build or use source, releases doesn't

### Usage:

#### Edit config.txt to match your pool:

`[Main]`    
`urlToPool:` **Pool URL, Ex: http://zec.suprnova.cc/**    
`PoolName:` **Pool Name, Ex: ZEC Suprnova**    
`CurrencyShortName:` **Currency Short Name, Ex: ZEC**    
`CoinMarketCapCurrencyName:` **CoinMarketCap.com Currency Name, Ex: ZCash**    
`AvailableBlocksInStats:` **Available Blocks In Pool Statistics, Ex: 20**    
__NOTE:__    
_AvailableBlocksInStats - you can get this value from pool > statistics > blocks_    

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

### Edits to not use the config.txt

1. Open ProfitCalc using Notepad++ or something like that. Python IDE is perfect

2. Change on top **UseConfig = 1** to **UseConfig = 0**

3. Fill values from config to the ProfitCalc.py
```
urlToPool = ""    
PoolName = ""    
CurrencyShortName = ""    
CoinMarketCapCurrencyName = ""    
AvailableBlocksInStats = 0    
```
4. Save and follow build instructions above, but config.txt is no longer required.

RELEASES Also Available


### How it works:  

Simply avg block time and avg reward....  
...and some simple maths...  



Donate (BTC): 1GEPkNwzTdwuNbPAwYF5LnRfgMhS4g7mmi