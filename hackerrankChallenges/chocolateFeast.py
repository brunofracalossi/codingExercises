money   = 43203
price   = 60
wrapper = 5    
    
n_buy = money / price

exchange = n_buy / wrapper
unused   = n_buy % wrapper

n_buy    = n_buy + exchange

while (unused + exchange) >= wrapper:
	exchange     = (unused + exchange) / wrapper
	unused       = n_buy % wrapper
	n_buy 		 = n_buy + exchange

print n_buy
