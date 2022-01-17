def rob(arr):
  if len(arr) == 0:
    return 0
  if len(arr) == 1:
    return arr[0]
  dp = arr[:]
  dp[0] = arr[0]
  dp[1] = max(arr[0],arr[1])
  for i in range(2,len(arr)):
    dp[i] = max(arr[i]+ dp[i-2], dp[i-1])
  return dp[len(arr)-1]  

print(rob([2,7,9,3,1]))  
