def maxProfit(prices: list) -> int:
    if (len(prices) == 1):
        return 0
    
    # Initialise
    if (prices[1] < prices[0]):
        min_price = prices[1]
        max_price = prices[1]

    else:
        min_price = prices[0]
        max_price = prices[1]

    max_profit = max_price - min_price
    for k in range(1,len(prices)-1):
        if (prices[k+1] < prices[k]):
            if (prices[k+1] < min_price):
                min_price = prices[k+1]
                max_price = prices[k+1]
        else:
            min_price = min(min_price,prices[k])
            max_price = max(max_price,prices[k+1])
        max_profit = max(max_profit, max_price - min_price)
    
    return max_profit
        
if __name__ == '__main__':
    prices = [7,6,5,4,3,2,1]
    print(maxProfit(prices))