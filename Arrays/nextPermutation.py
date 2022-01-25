#The approach
# 1. Loop from right to left till you find the first decreasing number d
# Example :  1 5 8 4 7 6 5 3 1 , first decreasing number from the right to left is 4
# 2. After this, go to the right and find the next largest number after d, call it i 
# Example :  1 5 8 4 7 6 5 3 1 ,the next greatest number after 4 to the right is 5
# 3. Swap the values of d and i 
# Example : 1 5 8 4 7 6 5 3 1  becomes 1 5 8 5 7 6 4 3 1 
# 4. Reverse from d + 1 to the end (from index 4 to 8)
# Example : 1 5 8 4 1 3 4 6 7 -> this is the next permutation
def nexp(nums):
    inv = len(nums) -2
    while (inv >= 0 and nums[inv] >= nums[inv+1]):
        inv -=1
    if inv < 0 :
        return nums.sort()
        
    for i in reversed(range(inv,len(nums))):
        if nums[i] > nums[inv]:
            #swap
            nums[i] , nums[inv]= nums[inv], nums[i]
            break
    #reverse the array from the inverse
    nums[inv+1: ] = nums[inv+1:][::-1]
    return nums

print(nexp([3,2,1]))              