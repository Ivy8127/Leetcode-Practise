class Solution:
    def isPalindrome(self, s: str) -> bool:
        #convert the string into lowercase characters
        palindrome = ''
        if s == "":
            return True
        for char in s.lower():
            if char.isalnum():
                palindrome += char
        reversed_word = palindrome[::-1]
        if reversed_word == palindrome:
            return True
        else:
            return False