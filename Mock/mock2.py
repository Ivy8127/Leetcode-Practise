
#problem  n = 3
#melborp
#m e l p r o b
#melprob
#word n = 1 len(str) - n
#dwor

def rotateArray(arr, n):
    res = []
    for i in range(len(arr)-1, len(arr)-1 -n,-1):

#first missing positive integer 
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1 2 0
        #3 4 -1 1     1 ..... 5
        #7 8 9 11 12  1 .....6
        #the smallest first missing integer is always 1
        #first missing positive integer should be in the range 1 - len(nums)+1 => 1 .... 4
        # negative numbers, 0 and values greater than the range serve no purpose, so convert them to 1
        # 1 2 1
        #3 4 1 1
        # 1 1 1 1 1
        containsOne = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                containsOne = 1
            elif nums[i]<=0 or nums[i] > len(nums):
                nums[i] = 1
        if containsOne == 0:
            return 1  
        # returns 1 if you scan through an array and never find 1 , like in 7,8,9,11,12
        #loop through array flipping signs
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            if nums[idx] > 0:
                nums[idx] = -1 * nums[idx]
        #-1 -2 1
        #-3 4 -1 -1 => 1 + 1 bc 4 is first nonnegative = 2 ans is 2

        # loop through array checking for the first non-negative number's index
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        #edge case, where all numbers are negative, return the len of arr + 1
        return len(nums) + 1

