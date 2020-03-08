class Stock:
    def __init__(self, name, shares, currSharePrice, prev4Days):
        self.name = name
        self.shares = shares
        self.currSharePrice = currSharePrice
        self.prev4Days = prev4Days

# methods for buying and selling stocks
    def buy(self, amount):
        if amount < 0:
            return

        # only buy a stock if we have the money to
        if m <= amount:
            print(self.name + " BUY " + str(amount))

    def sell(self, amount):
        if amount < 0:
            return

        # only sell if you have enough stock
        if self.shares <= amount:
            print(self.name + " SELL " + str(amount))

# this reads in the first line containing m (money for the day), k (number of stocks for the day) and d (number of remaining days to buy) values
firstLine = input().rsplit()

# variables allocated to 
m = int(firstLine[0])
k = int(firstLine[1])
d = int(firstLine[2])

# using d, iterate through the days (not certian if needed, but it threw errors when I had it in)
#for y in range(d):

# using k, iterate through the lines
lines = []
for x in range(k):
    lines.append(input())

# iterate through each line adding making an object for each stock
stocks = []
for x in range(k):
    seperate = lines[x].rsplit()
    #index 0 is name, 1 is shares owned, 6 is current stock price, 2 through 5 (inclusive) are the previous 4 days of stock price information
    stocks.append(Stock(seperate[0], seperate[1], seperate[6], (seperate[2], seperate[3], seperate[4], seperate[5])))

#buy usage
stocks[0].buy(10)
stocks[len(stocks) - 1].buy(3)