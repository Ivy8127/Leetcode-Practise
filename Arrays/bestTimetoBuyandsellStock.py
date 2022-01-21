def maxProfit(prices) -> int:
    if len(prices) == 0:
        return 0
    curr_min = prices[0]
    max_profit = 0
    for i in range(1,len(prices)):
        if prices[i] < curr_min:
            curr_min = prices[i]
        elif prices[i] - curr_min > max_profit:
            max_profit = prices[i] - curr_min
    return max_profit


print(maxProfit([7,1,5,3,6,4]))