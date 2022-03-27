#n = 3
# 0 1 2 3
#3,0,1
# 3: 1, 0:1, 1: 1
from collections import Counter
def missingNumbers(arr):
    m = Counter(arr)
    for i in range(len(arr)+1):
        if i not in m:
            return i

print(missingNumbers([3,0,1]))
#Time complexity o(n)
#Space complexity o(n)

# 0 1 2 3 = 6
#4 
#6-4 = 2 
#time(0(2n))
#space 0(1)
def missingN(arr):
    total = 0
    for i in range(len(arr)+1):
        total+= i
    return total - sum(arr)

print(missingN([3,0,1]))        

