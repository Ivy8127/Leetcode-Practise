class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l = [1]* len(nums)
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    l[i] = max(l[i], l[j]+1)
        return max(l) 
#idea is simple, compare the value at position j vs i ,
# if it's less than i then you want to return the maximum subsequence , 
# which is done by comparing the value at i vs the value at j plus 1 , in the new created list
# The longest increasing subsequence is the largest value in the list        