#O n^2 sln 
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #ths just like a filler value, to start the comparison with
        res = nums[0]+nums[1]+nums[2]
        nums.sort()
        #same old 2 pointer technique
        for i in range(len(nums)-2):
            #not inclusive bc the 2nd last element contains only 2 values to the last value
            #so it can't hold triplets!
            left = i+1
            right = len(nums)-1
            while left < right:
                threeClosest = nums[left] + nums[right] + nums[i]
                if threeClosest < target:
                    left +=1
                else:
                    right -=1
                #if the diff btwn the current sum and the target is smaller than the difference between the result and the target, set the currentsum value as the result
                if abs(threeClosest - target) < abs(res - target):
                    res = threeClosest
        return res           
        