from collections import Counter
#glorified 2sum problem
def findPairs(nums, k):
    count = 0
    hashmap = Counter(nums) #{3:1,1:2,4:1,5:1}
    if k==0:
        for key,v in hashmap.items():
            if v > 1:
                count +=1
    else:            
        for key,v in hashmap.items():
            if key +k in hashmap:
                count +=1
            
    return count 

print(findPairs([1,2,3,4,5],1))    