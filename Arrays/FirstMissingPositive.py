class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        #step 1 - loop through array removing -negatives, > n and 0s and changing to 1
        containsOne = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                containsOne = 1
            elif (nums[i]<= 0 or nums[i] > len(nums)):
                nums[i] =1
        if containsOne == 0:
            return 1
        #1,2,1
        #step 2, loop through the array and flip the numbers to negative
        for i in range(len(nums)):
            index = abs(nums[i]) -1 
            #if the number is not negative, flip it to be negative, otherwise,leave it
            if nums[index] > 0:
                nums[index] = -1 * nums[index]
         #-1,-2, 1       
        #step 3, loop through array looking for the first smallest positive int
        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        #edge case where all values are negative
        return len(nums)+1
        
        
                
        