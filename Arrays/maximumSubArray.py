#Brute force method O(n^2) - Time complexity
import numpy as np
def maxSubArray(nums):
        ans = -np.inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans

#Kadane's algorithm O(n) -Time complexity
def maxSubArray(arr):
    max_sub_array = curr_max = arr[0]
    for i in range(1,len(arr)-1):
        curr_max = max(arr[i], max_sub_array + arr[i])

        if curr_max > max_sub_array:
            max_sub_array = curr_max
    return max_sub_array        

print(maxSubArray([-2,2,5,-11,6]))        