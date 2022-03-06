#Time complexity O(n)
#using 2 pointer technique

def validPalindrome( s):
    if len(s) < 2:
        return True
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left+= 1
            right -=1
        else:
            #delete the left and right pointer to check whether it is a palindrome
            return s[left+1:right+1]
    return True 
print(validPalindrome('abca'))   
# a b c a
#   s e 
# left -? right -> b => b leaving  a c a -> return true bc it is a palindrome when reversed
# left + 1 right + 1 => c leaving a b a -> returns true bc it is a palindrome when reversed
        
        