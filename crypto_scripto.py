import requests
import json
import datetime
import prices

def main():
	command = input("What would you like to do?...\n (s)ee current prices, (c)alculate portfolio value, or (e)xit...").lower()
	if command == "s":
		print("BTC: $" + str(prices.BTC_price) + "\n" + "LTC: $" + str(prices.LTC_price) + "\n" + "BCH: $" + str(prices.BCH_price) + "\n" + "ETH: $" + str(prices.ETH_price))
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
	BTC_value = prices.BTC_price * BTC_quant
	BCH_value = prices.BCH_price * BCH_quant
	LTC_value = prices.LTC_price * LTC_quant
	ETH_value = prices.ETH_price * ETH_quant
	wallet_value = BTC_value + BCH_value + LTC_value + ETH_value
	
	#PRINTS
	print(str(datetime.time))
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
	BTC_value = prices.BTC_price * BTC_quant
	BCH_value = prices.BCH_price * BCH_quant
	LTC_value = prices.LTC_price * LTC_quant
	ETH_value = prices.ETH_price * ETH_quant
	wallet_value = BTC_value + BCH_value + LTC_value + ETH_value
	
	#PRINTS
	print(datetime.now())
	print("Wallet value: $" + str(wallet_value))
	return

main()
