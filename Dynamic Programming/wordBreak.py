
def wordBreak(s, wordDict):
    dp =[False] * (len(s)+1) #accounting for the value after the last index
    dp[len(s)] = True #Base case
    for i in range(len(s)-1,-1,-1):
        for word in wordDict:
            if (i + len(word) <= len(s) and s[i:i+len(word)] == word):
                dp[i] = dp[i+ len(word)]
            if dp[i]:
                break
    return dp[0]            
        

print(wordBreak('leetcode',['leet','code']))  #returns True  