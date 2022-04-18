import math

def findTwoSumClosest(nums, target):
    min_diff = abs(float('inf') - target)
    bstart, bEnd = 0,0
    start = 0
    end = len(nums) - 1

    while start < end:
        summ = nums[start] + nums[end]
        diff = abs(summ - target)
        if diff < min_diff:
            min_diff = diff
            bstart = start
            bEnd = end

        if summ > target:
            end -= 1
        if summ < target:
            start += 1

    return [nums[bstart], nums[bEnd]]

print(findTwoSumClosest([1, 2, 3, 4, 5], target = 10))    
print(findTwoSumClosest([-1, 2, 1, -4], target = 4))    
print(findTwoSumClosest([10, 22, 28, 29, 30, 40], target = 54))    