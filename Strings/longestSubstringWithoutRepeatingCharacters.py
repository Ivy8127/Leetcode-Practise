#Sliding window + set technique
def lengthOfLongestSubstring( s):
    res = 0
    left = 0
    charSet = set()
    
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left +=1
            
        charSet.add(s[right])
        res = max(res, len(charSet))
    return res    
print(lengthOfLongestSubstring("pwwkew")) #3  
