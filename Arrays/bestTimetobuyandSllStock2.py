#Same as buying and selling stock version 1, with a little twist
def maxProfit(prices) -> int:
    maxProfit = 0
    minPrice = prices[0]
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        if prices[i] - minPrice > 0:
            maxProfit += prices[i] - minPrice
        minPrice = prices[i]    
            
            
    return maxProfit 

print(maxProfit([7,1,5,3,6,4]))     #answer is 7       
        