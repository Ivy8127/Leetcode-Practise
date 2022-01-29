def threeSum(nums):
    res = []
    nums.sort() #to remove duplicates
    for i,num in enumerate(nums):
        if i > 0 and num == nums[i-1]: #this is a duplicate therefore skip it
            continue
        left , right = i + 1 , len(nums)-1
        while left < right:
            threesum = num + nums[left] + nums[right]
            if threesum > 0: #decrease the sum by decrementing the right pointer bc array is sorted
                right -= 1
            elif threesum < 0 : #increase the sum by incrementing the left pointer bc the array is sorted
                left +=1
            else : #sum is 0 in which case , we've found our answer
                res.append([num,nums[left],nums[right]])
                #update your left pointer
                left +=1
                #we want to remove duplicates incase the current left pointer value 
                # as the previous , bc they will yield the same value
                while left < right and nums[left] == nums[left-1]:
                    #move to the next left pointer
                    left +=1
    return res  

print(threeSum([-1,0,1,2,-1,-4]))                  

