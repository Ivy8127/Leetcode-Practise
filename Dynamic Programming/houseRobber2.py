#Same approach as house robber 1, only difference is to create 2 subarrays
#One includes the first house without the last and the other includes the last house without the first
#bc they're adjacent to each other in a circle
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