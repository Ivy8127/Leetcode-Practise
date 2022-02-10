def validAnagrams(s,t):
    s = sorted(s)
    t = sorted(t)
    if s==t:
        return True
    return False
print(validAnagrams("nat","bat"))#False 


#Approach 2 - hashmaps
def validA(s,t):
    anagrams = {}
    #populate a hashmap with string s characters
    for char in s:
        if char in anagrams:
            anagrams[char]+=1
        else:
            anagrams[char] = 1

    for char in t:
        if char in anagrams:
            anagrams[char] -= 1
        else:
            return False #char is not an anagram bc it's not contained in hashmap
    for k,v in anagrams.items():
        if v == 0: #matching charater numbers
            return True  
    return False                  

print(validAnagrams("nat","tan"))#True        

