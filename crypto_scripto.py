import urllib2
from bs4 import BeautifulSoup
import datetime

def main():
	command = input("What would you like to do?...\n (s)ee current prices, (c)alculate portfolio value, or (e)xit...").lower()
	if command == "s":
		print("BTC: $" + str(BTC_stripped) + "\n" + "LTC: $" + str(LTC_stripped) + "\n" + "BCH: $" + str(BCH_stripped) + "\n" + "ETH: $" + str(ETH_stripped))
		main()
	elif command == "c":
		identity_check()
	elif command == "e":
		return
	else:
		print("Invalid input: please select one of the choices" + "\n")
		main()
	return
	
def identity_check():
	name = input("Please enter your name...")
	if name.lower() == "ian":
		ian_wallet()
		main()
	else:
		guest_wallet(name)
		main()

def ian_wallet():
	#Wallet amounts
	BTC_quant = 0.496
	LTC_quant = 9.00727417
	BCH_quant = 0.23084719
	ETH_quant = 0.31473064

	#Calculations
	BTC_value = BTC_stripped * BTC_quant
	BCH_value = BCH_stripped * BCH_quant
	LTC_value = LTC_stripped * LTC_quant
	ETH_value = ETH_stripped * ETH_quant
	wallet_value = BTC_value + BCH_value + LTC_value + ETH_value
	
	#PRINTS
	print(str(now))
	print("Wallet value: $" + str(wallet_value))

def guest_wallet(name):
	print("Welcome " + name)
	if input("Do you have BTC? (Y or N)...") == "Y":
		BTC_quant = float(input("How much?..."))
	else: BTC_quant = 0.0

	if input("Do you have BCH? (Y or N)...") == "Y":
		BCH_quant = float(input("How much?..."))
	else: BCH_quant = 0.0

	if input("Do you have LTC? (Y or N)...") == "Y":
		LTC_quant = float(input("How much?..."))
	else: LTC_quant = 0.0

	if input("Do you have ETH? (Y or N)...") == "Y":
		ETH_quant = float(input("How much?..."))
	else: ETH_quant = 0.0

	#Calculations
	BTC_value = BTC_stripped * BTC_quant
	BCH_value = BCH_stripped * BCH_quant
	LTC_value = LTC_stripped * LTC_quant
	ETH_value = ETH_stripped * ETH_quant
	wallet_value = BTC_value + BCH_value + LTC_value + ETH_value
	
	#PRINTS
	print(str(now))
	print("Wallet value: $" + str(wallet_value))
	return

#BTC
CoinBase_BTC_url = "https://coinmarketcap.com/currencies/bitcoin/"
page = urllib2.urlopen(CoinBase_BTC_url)
soup = BeautifulSoup(page, 'html.parser')
now = datetime.datetime.now()

BTC_price = soup.find(attrs={'class': "text-large2"})
BTC_stripped = float(BTC_price.text.strip())

#BCH
CoinBase_BCH_url = "https://coinmarketcap.com/currencies/bitcoin-cash/"
page = urllib2.urlopen(CoinBase_BCH_url)
soup = BeautifulSoup(page, 'html.parser')

BCH_price = soup.find(attrs={'class': "text-large2"})
BCH_stripped = float(BCH_price.text.strip())

#LTC
CoinBase_LTC_url = "https://coinmarketcap.com/currencies/litecoin/"
page = urllib2.urlopen(CoinBase_LTC_url)
soup = BeautifulSoup(page, 'html.parser')

LTC_price = soup.find(attrs={'class': "text-large2"})
LTC_stripped = float(LTC_price.text.strip())

#ETH
CoinBase_ETH_url = "https://coinmarketcap.com/currencies/ethereum/"
page = urllib2.urlopen(CoinBase_ETH_url)
soup = BeautifulSoup(page, 'html.parser')

ETH_price = soup.find(attrs={'class': "text-large2"})
ETH_stripped = float(ETH_price.text.strip())

main()
