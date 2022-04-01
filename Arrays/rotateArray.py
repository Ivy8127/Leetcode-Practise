#Time complexity - linear time
#Space complexity - linear time
def rotate(nums, k):
    rotateArr = [0]*(len(nums))
    for i in range(len(nums)):
        if (i+k) < len(nums):
            rotateArr[i+k] = nums[i]
        else:
            idx = (i+k) % len(nums)
            rotateArr[idx] = nums[i] 
    nums = rotateArr[:]           
    return nums

print(rotate([1,2,3,4,5],k =2))    
print(rotate([1,2,3,4,5,6,7], k = 3))  
print(rotate([-1,-100,3,99], k = 2))  
