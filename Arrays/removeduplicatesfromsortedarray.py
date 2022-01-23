#Non-optimal sln - not to be used in an interview situation
class Solution:
    def removeDuplicates(self, nums) :
        unique_nums = sorted(list(set(nums)))
        k = len(unique_nums)
        for i in range(k):
            nums[i] = unique_nums[i]
        return k
    

#Optimal solution space O(1)
#Time complexity O(n)
#approach 2 - 2 pointer technique
#the left pointer will always keep track of the count of the unique elements in the input array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        left = 1
        
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left +=1
        return left


