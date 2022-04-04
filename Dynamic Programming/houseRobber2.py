#Same approach as house robber 1, only difference is to create 2 subarrays
#One includes the first house without the last and the other includes the last house without the first
#bc they're adjacent to each other in a circle

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob1(nums[:-1]), self.rob1(nums[1:]))
    
    def rob1(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        dp = nums[:]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+ dp[i])
        return dp[len(nums)-1]





def rob(nums):
    return max(nums[0],helper(nums[:-1]),helper(nums[1:]))
    
def helper(nums):
    rob1 , rob2 = 0,0
    for n in nums:
        newrob = max(rob1+ n , rob2)
        rob1 = rob2
        rob2 = newrob
    return rob2
print(rob([1,2,3,4]))  #6  