class sumCoins:

    def __init__(self, coins_array):
        self.coins = coins_array
        

    def getMinCoins(self, sum_coins):
    	min_coins = 0
    	total     = 0
    	size      = len(self.coins)

    	while total != sum_coins:
    		ind = size - 1

    		while ind >= 0:
    			if (self.coins[ind] <= (sum_coins - total)):
    				total = total + self.coins[ind]
    				min_coins = min_coins + 1
    				ind = size
    				print "Total: " + str(total)

    			ind = ind -1

    	return min_coins

#test = [1,3]
#print sumCoins(test).get_min_coins(0)