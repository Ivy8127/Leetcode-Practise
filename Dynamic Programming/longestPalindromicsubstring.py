#Time complexity O(n^2)
#Approach:
# we have 2 ways of checking whether a word is a palindrome or not
# 1.check from the outer going in, if they match, loop inside
# 2. check from the center and loop outwards using left and right pointers, if they are the same
#it is a palindrome
def lps(s):
    res = ""
    res_len = 0
    for i in range(len(s)):
        #for odd length strings
        left , right = i,i
        while left >= 0 and right < len(s) and s[left] == s[right]: #checking that it's a palindrome
            if right - left + 1 > res_len:
                res = s[left:right +1]
                res_len = right - left + 1

            left -= 1 # moves outwards to the left
            right += 1 # moves outwards to the right
        left , right = i,i +1
        #for even length strings
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > res_len:
                res = s[left:right +1]
                res_len = right - left + 1

            left -= 1
            right += 1
    return res              
print(lps('cbbd'))    