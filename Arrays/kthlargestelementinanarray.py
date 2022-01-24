#Approach 1  - Best approach using a heap ,more efficient Time complexity O(nlogk), 
#space complexity O(k)
import heapq as hq
def k(nums,k):
    heap = []
    for num in nums:
        hq.heappush(heap,num)    
        if len(heap) > k:
           hq.heappop(heap)
    return heap[0] 
print(k([3,2,1,5,6,4],2))            


#Approach 2 Time complexity O(nlogn)
def findKthLargest(nums, k):
        if len(nums) == 0:
            return 0
        if k > len(nums):
            return
        nums = sorted(nums, reverse=True)
        return nums[k-1]

print(findKthLargest([3,2,1,5,6,4],2))        