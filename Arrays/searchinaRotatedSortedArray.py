
""" We need to search left or right, however, if rotation
is on one side or the other, we can only check the non-rotated side
so if mid is not the num then we check which side is non rotated
and see if target exists in that non rotated side
if it does, go that way,
if not then we go other other way and hope we find it there
 """

def search(nums, target):
    #binary search
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        #left sorted array
        if nums[mid] >= nums[left]:
            if nums[mid] < target or target < nums[left]:
                left = mid + 1
            else:
                right = mid -1
        #Right sorted array    
        else:
            if nums[mid] > target or target > nums[right]:
                
                right = mid -1
            else:
                left = mid + 1
    return -1   

print(search([4,5,6,7,0,1,2],0))    #returns 4 bc 0 is in index 4
print(search([4,5,6,7,0,1,2],3))    #returns -1 bc 3 is not in the list

def search(nums, target):
    #binary search
    left = 0
    right = len(nums)-1
    
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        #left sorted array
        if nums[mid] >= nums[left]:
            if nums[mid] < target or target < nums[left]:
                left = mid + 1
            else:
                right = mid -1
        #Right sorted array    
        else:
            if nums[mid] > target or target > nums[right]:
                
                right = mid -1
            else:
                left = mid + 1
    return -1  