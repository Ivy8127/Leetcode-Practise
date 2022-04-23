from collections import Counter
import heapq
def topKFrequent(nums, k):
    if k == len(nums):
        return nums
    #create a counter
    count = Counter(nums)
    
    #create a max heap
    mx_heap = []
    for key,val in count.items():
        mx_heap.append((-val,key))
        # 1: 3 2: 2 3: 1
        #[(-3 : 1 ),( -2, 2), (-1, 3)]
    heapq.heapify(mx_heap)
    res = []
    for _ in range(k):
        res.append(heapq.heappop(mx_heap)[1])
        
    return res
print(topKFrequent([1,1,1,2,2,3],k=2))