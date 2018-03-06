import krakenex

k = krakenex.API()
k.load_key('kraken.key') #To run the code, you are required to have a separate file containing your Kraken API keys.
whatYouWantToOwn = 0.01 #This is how much you want to own of every currency, measured in BTC price.
sellFactor = 1.2 #This indicates how much the value of each currency has to increase or decrease in order to trigger a sell message. A sellFactor of 1.2 triggers a sell message if the currency's value increases by 20%.

#print(k.query_private('Balance'))
#print(k.query_public('Ticker', {'pair': 'XXBTZEUR'})['result']['XXBTZEUR']['c'][0])

def price(currency):
	success = False
	while success == False:
		try:
			if currency == "XXBT":
				return 1
			elif currency == "ZEUR":
				return 1/float(k.query_public('Ticker', {'pair': "XXBTZEUR"})['result']["XXBTZEUR"]['c'][0])
			elif currency == "XXBTZEUR":
				return float(k.query_public('Ticker', {'pair': "XXBTZEUR"})['result']["XXBTZEUR"]['c'][0])
			else:
				currencies = {"Bitcoin-Cash": "BCHXBT", "BCH": "BCHXBT", "Dash": "DASHXBT", "DASH": "DASHXBT", "EOS": "EOSXBT", "Ethereum-Classic": "XETCXXBT", "XETC": "XETCXXBT", "Ethereum": "XETHXXBT", "XETH": "XETHXXBT", "Gnosis": "GNOXBT", "Iconomi": "XICNXXBT", "Litecoin": "XLTCXXBT", "XLTC": "XLTCXXBT", "Melon": "XMLNXXBT", "Augur": "XREPXXBT", "XREP": "XREPXXBT", "Dogecoin": "XXDGXXBT", "XXDG": "XXDGXXBT", "Stellar": "XXLMXXBT", "XXLM": "XXLMXXBT", "Monero": "XXMRXXBT", "XXMR": "XXMRXXBT", "Ripple": "XXRPXXBT", "XXRP": "XXRPXXBT", "Zcash": "XZECXXBT", "XZEC": "XZECXXBT"}
				return float(k.query_public('Ticker', {'pair': currencies[currency]})['result'][currencies[currency]]['c'][0])
		except:
			pass

currencies = {"ZEUR": "Euro            ", "XXBT": "Bitcoin         ", "XXRP": "Ripple          ", "XLTC": "Litecoin        ", "XETH": "Ethereum        ", "XETC": "Ethereum-Classic", "XREP": "Augur           ", "XXDG": "Dogecoin        ", "XXLM": "Stellar         ", "XZEC": "Zcash           ", "XXMR": "Monero          ", "DASH": "Dash            ", "EOS": "EOS             ", "BCH": "Bitcoin-Cash    "}
success = False
while success == False:
	try:
		balanceDictionary = k.query_private('Balance')['result']
		success = True
	except:
		pass
print("##########################################################################################")
print("########################### ØYVIND'S AWESOME TRADING ALGORITHM ###########################")
print("##########################################################################################")
print("------------------------------------------------------------------------------------------")
totalAmount = 0
for ticker in balanceDictionary:
	amountInBitcoin = float(balanceDictionary[ticker])*price(ticker)
	totalAmount += amountInBitcoin
	if ticker == "XXBT" or ticker == "ZEUR":
		sellMessage = ""
	elif amountInBitcoin < 0.0001:
		sellMessage = "          You don't own any of this currency"
	elif amountInBitcoin > whatYouWantToOwn*sellFactor:
		sellMessage = "          Sell " + format(amountInBitcoin-whatYouWantToOwn, '.10f') + " BTC worth of " + currencies[ticker]
	elif amountInBitcoin < whatYouWantToOwn/sellFactor:
		sellMessage = "          Buy " + format(whatYouWantToOwn-amountInBitcoin, '.10f') + " BTC worth of " + currencies[ticker]
	else:
		sellMessage = ""
	if ticker != "ZEUR":
		print(currencies[ticker] + " " + format(amountInBitcoin, '.4f') + " BTC" + sellMessage)
		print("------------------------------------------------------------------------------------------")
print("Total            " + format(totalAmount, '.4f') + " BTC (= " + format(totalAmount*price("XXBTZEUR"), '.2f') + " EUR)")
print("------------------------------------------------------------------------------------------")
