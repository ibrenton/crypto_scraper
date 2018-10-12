#Pull and calculate prices using requests library and https://min-api.cryptocompare.com/ instead of scraping using bs4
import requests
import json

r = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,BCH,LTC&tsyms=USD').json()
BTC_price = r['BTC']['USD']
ETH_price = r['ETH']['USD']
BCH_price = r['BCH']['USD']
LTC_price = r['LTC']['USD']