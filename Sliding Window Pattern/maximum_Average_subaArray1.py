class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #sliding window approach
        #idea is to remove the left most value an adding the new
        #right most value into the window
        #step 1 calculate first window
        res = sum(nums[:k])
        max_res = res
        for i in range(len(nums)-k):
            #delete first element from window an add next element into it
            res = res - nums[i] + nums[i+k]
            max_res = max(max_res, res)
        return max_res/k    
            
        
        