#binary search - O log n time
#Our array is sorted and rotated, we need to find the minimum number
#check that the mid number is greater than the right pointer value, if it is
#this means that our min value is on the right, shift left pointer to begin
#binary search there, otherwise,shift right pointer to mid to begin binary search 
#on the left subarray
#hmm.. did this question today and i don't get it. Will have to look at it tomorrow again
def findMin( nums):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right) //2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid         #5
                            #4             #2 
    return nums[left]  #3           #1 
print(findMin([3,4,5,1,2]))          
        