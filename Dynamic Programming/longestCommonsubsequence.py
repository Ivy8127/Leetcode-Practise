def lcs(text1, text2):
    #create a 2d dp grid
    #text2 number of columns
    #text1 number of rows
    dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]

    for i in range(len(text1)):
        for j in range(len(text2)):
            if text1[i] == text2[j]: #text values match
                dp[i][j] = 1 + dp[i-1][j-1]
            else: #text values don't match and therefore compete
                dp[i][j] =max(dp[i][j-1], dp[i-1][j])    
    return dp[i][j]

print(lcs("abc","def"))    