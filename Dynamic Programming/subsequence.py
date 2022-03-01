
#Find the subsequences in a string -> 2**n
import itertools

def find_subsequence(str):
    combs = []
    for x in range(1,len(str)+ 1):
        combs.append(list(itertools.combinations(str,x)))
    l2 = []    
    for c in combs:
        for t in c:
            l2.append(''.join(t))  
    return l2         

print(find_subsequence('abc'))  

#method 2 -> Pick and don't pick concept
def subsequence(str, output):
    if len(str) == 0:
        print(output)
        return
    subsequence(str[1:], output + str[0])
    subsequence(str[1:], output)
print(subsequence('abcd',''))    
