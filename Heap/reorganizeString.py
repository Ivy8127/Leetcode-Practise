from collections import Counter
import heapq

def reorganizeString(s):
    count = Counter(s)
    #add allvalues to a maxheap
    maxHeap = [[-cnt,char] for char, cnt in count.items()]
    #heapify the maxheap
    heapq.heapify(maxHeap)
    
    prev = None
    res = ""
    while maxHeap or prev:
        if prev and not maxHeap:
            return ""
        cnt, char = heapq.heappop(maxHeap)
        res += char
        cnt += 1
        if prev:
            heapq.heappush(maxHeap,prev)
            prev = None
        if count!= 0:
            prev = [cnt,char]
    return res  

print(reorganizeString("aab"))          
        