def numDecodings(s):
    dp = [0] * (len(s)+1)
    dp[0] =1 #accomodating an empty string
    
    #base case
    if s[0] == '0':
        return 0
    else:
        dp[1] = 1 #if the first string character is not a 0, you can only decode it once
        
    for i in range(2, len(s)+1) :
        #4cases
        #Case 3 : value at i-1 is 0 and 0-2 is 1 or 2 meaning that it's within 26
        #- decode in 1 way - taking the whole number as 1 way eg 20
        if s[i-1] == '0':
            if s[i-2] == '1' or s[i-2] == '2':
                dp[i] = dp[i-2]
            else:
                #case 4 , number is past 26 therefore can't be decoded .eg 60
                return 0 
        else:
            #case 1 : value between 10 and 26 - decode in 2 ways
            if s[i-2] == "1" or s[i-2] == "2" and int(s[i-1]) < 7:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                #case 2 : value is greater than 26 - decode in 1 way
                dp[i] = dp[i-1]
    return dp[len(s)]            
                
print(numDecodings("12")) # 1, 2 or 12 -> can be decoded in 2 ways #2                
        