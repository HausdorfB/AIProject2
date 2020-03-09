import numpy as np

def previousPrice(currSharePrice):
    #Returns either 0 or 1. 0 means share is at maximum currently. 
    #The closer to 1, the higher the lastPr value with respect to the trend in the period.
    
    # Max and min value in the period of 4 days
    minPr = currSharePrice.min()
    max_price = currSharePrice.max()
    
    if (max_price == minPr):
        return 0
        
    return abs(currSharePrice[-1] - minPr)/(max_price - minPr)
    

"""
    Variable legend:
	m - money for the day (float)
	k - number of stocks for the day (int)
	d - number of remaining days to buy (int)
    name - Stock name (String Array)
    shares - Stock shares (int Array)
    currSharePrice - Prices for each day containing price and priority(4 days)(2d int array)
"""
	
#Function that prints out transactions (buy_Sell)
#!/usr/bin/py
def printbuy_Sell(m, k, d, name, shares, currSharePrice):
    
	#Create array for available stock buy options
	options = [] 
	#Array for when stocks are bought/sold
	buy_Sell = []
	#Buying threshold 
    threshold = 0.60 
    currSharePrice = np.array(currSharePrice)
	deviations = currSharePrice.std(1) 
    
    #Stocks with higher deviations sell for more
    #Reverse list of deviatons - higher deviations = more desirable
	for i in reversed(np.argsort(deviations)): 
        
		#Contrast represents the numbers in comparison to one another
        contrast = previousPrice(currSharePrice[i])
        
        #Sell stock if the contrast between the currently held and lastPr price is high (positive gain)
        if (contrast >= threshold and shares[i] > 0):
            buy_Sell.append(name[i] + ' SELL ' + str(shares[i]))
        
        #add to the "options" array if the contrast between the currently held and lastPr price is low (Can have positive gain)
        if (contrast <=(1-threshold)):
            options.append((i, currSharePrice[i][-1]))
            
    #Cycle through the "options" array and buy a limit of "m" worth of stocks
    for i, lastPr in options:
               
        #Amount of "Buy's"
        amount = int(m/lastPr)
        if amount:
            buy_Sell.append(name[i] + ' BUY ' + str(amount))
            #update "m"
            m -= amount * lastPr
            
	#Print stocks purchased
    print(len(buy_Sell))
    for t in buy_Sell:
        print(t) 


if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    name = []
    shares = []
    currSharePrice = []
    for data in range(k):
        temp = raw_input().strip().split()
        name.append(temp[0])
        shares.append(int(temp[1]))
        currSharePrice.append([float(i) for i in temp[2:7]])

    printbuy_Sell(m, k, d, name, shares, currSharePrice)
