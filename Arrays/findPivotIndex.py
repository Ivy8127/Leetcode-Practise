
#the idea is that the right sum is equal to the total sum - the current index value - the left sum
#if the right sum and left sum are equal , return that index
#make sure to always increment the left sum though
#if you never get a pivot index return -1
def pivotIndex(nums):
    totalSum = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        if leftSum == (totalSum - leftSum - nums[i]):
            return i
        leftSum += nums[i]
    return -1  

print(pivotIndex([1,7,3,6,5,6])) #6 is the pivot value therefore return it's index 3
    
