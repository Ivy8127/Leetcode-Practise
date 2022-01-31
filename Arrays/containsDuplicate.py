
def containsDuplicate(nums):
    num_S = set(nums)
    if len(num_S) == len(nums):
        return False
    return True
    
print(containsDuplicate([1,2,3,4,1]))   
#or
def cd(nums):
    num_s = set()
    for i in range(len(nums)):
        if nums[i] in num_s:
            return True
        else:
            num_s.add(nums[i])
    return False 

print(cd([1,2,3,4]))               