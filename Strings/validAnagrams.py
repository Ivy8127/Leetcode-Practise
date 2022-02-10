def validAnagrams(s,t):
    s = sorted(s)
    t = sorted(t)
    if s==t:
        return True
    return False
print(validAnagrams("nat","bat"))#False        
print(validAnagrams("nat","tan"))#True        