def findKthLargest(nums, k):
        if len(nums) == 0:
            return 0
        if k > len(nums):
            return
        nums = sorted(nums, reverse=True)
        return nums[k-1]

print(findKthLargest([3,2,1,5,6,4],2))        