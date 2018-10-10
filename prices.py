import urllib.request
from bs4 import BeautifulSoup
import datetime

#BTC
CoinBase_BTC_url = "https://coinmarketcap.com/currencies/bitcoin/"
page = urllib.request.urlopen(CoinBase_BTC_url)
soup = BeautifulSoup(page, 'html.parser')
now = datetime.datetime.now()

BTC_price = soup.find(attrs={'class': "text-large2"})
BTC_stripped = float(BTC_price.text.strip())

#BCH
CoinBase_BCH_url = "https://coinmarketcap.com/currencies/bitcoin-cash/"
page = urllib.request.urlopen(CoinBase_BCH_url)
soup = BeautifulSoup(page, 'html.parser')

BCH_price = soup.find(attrs={'class': "text-large2"})
BCH_stripped = float(BCH_price.text.strip())

#LTC
CoinBase_LTC_url = "https://coinmarketcap.com/currencies/litecoin/"
page = urllib.request.urlopen(CoinBase_LTC_url)
soup = BeautifulSoup(page, 'html.parser')

LTC_price = soup.find(attrs={'class': "text-large2"})
LTC_stripped = float(LTC_price.text.strip())

#ETH
CoinBase_ETH_url = "https://coinmarketcap.com/currencies/ethereum/"
page = urllib.request.urlopen(CoinBase_ETH_url)
soup = BeautifulSoup(page, 'html.parser')

ETH_price = soup.find(attrs={'class': "text-large2"})
ETH_stripped = float(ETH_price.text.strip())