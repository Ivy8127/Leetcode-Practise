#Time complexity O(n)
#using 2 pointer technique
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left+= 1
                right -=1
            else:
                #delete the left and right pointer
                return s[left+1:right+1] == s[left+1:right+1][::-1] or s[left:right] == s[left:right][::-1]
        return True        
        