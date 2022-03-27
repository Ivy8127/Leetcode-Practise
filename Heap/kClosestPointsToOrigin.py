class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # [[1,3],[-2,2]] k = 1
        #root 10 vs root 8 [[-2,2]]
        #minheap
        # [[10, 1,3], [8, -2,2]]
        minHeap = []
        for x,y in points:
            dist = (x*x) + (y*y)
            minHeap.append([dist, x,y])
            
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k-=1
        return res