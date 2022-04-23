from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # {i : 2, leetcode : 1, love : 2, coding : 1 } k = 2
        count = Counter(words)
        max_heap = []
        for key , val in count.items():
            max_heap.append((-val,key))
            
        heapq.heapify(max_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res   
        
        
        