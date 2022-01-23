#we want to find the minimum amount of coins required to satisfy the amount
#Time complexity O(A*C)
#Space complexity O(A)
def coinChange( coins, amount):
    #initialize your dp array to the value of the ammount
    #remembering that plus 1 is bc it's zero indexed
    dp = [amount+1] * (amount + 1)
    
    dp[0] = 0 #sub problem
    for amount in range(amount +1):
        for c in coins:
            if amount - c >= 0:
                dp[amount] = min(dp[amount], dp[amount-c]+1)
                
    return dp[amount] if dp[amount] != amount + 1 else -1  


print(coinChange([1,2,5],11))      
