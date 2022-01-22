#First approach works but not efficient for large input strings
def find_anagrams(s,p):
    anagram = []
    for i in range(len(s) - len(p)+1):
        substr = s[i:i+ len(p)]
        if sorted(substr) == sorted(p):
            anagram.append(i)
    return anagram        
print(find_anagrams("abcdecdbacb","cab")) 

#sliding window approach - most efficient
def find_anagrams(s,p):
    if len(p)> len(s):
        return []
    pcount, scount = {},{}
    for i in range(len(p)):
        pcount[p[i]] = 1 + pcount.get(p[i],0)
        scount[s[i]] =1 + scount.get(s[i],0)
    #pcount {'a': 1 
    # 'b':1 , 'c':1} => same to scount
    res = []
    if pcount == scount:
        res.append(0)
    left = 0
    for right in range(len(p),len(s)):
        scount[s[right]] = 1 + scount.get(s[right],0)
        scount[s[left]]-=1 #a : 0
        if scount[s[left]]==0:
            scount.pop(s[left])
        left += 1
        if scount == pcount:
            res.append(left) 
    return res
print(find_anagrams("abcdecdbacb","cab"))                
