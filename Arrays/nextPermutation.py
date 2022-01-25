#The approach
# 1. Loop from right to left till you find the first decreasing number d
# Example :  1 5 8 4 7 6 5 3 1 , first decreasing number from the right to left is 4
# 2. After this, go to the right and find the next largest number after d, call it i 
# Example :  1 5 8 4 7 6 5 3 1 ,the next greatest number after 4 to the right is 5
# 3. Swap the values of d and i 
# Example : 1 5 8 4 7 6 5 3 1  becomes 1 5 8 5 7 6 4 3 1 
# 4. Reverse from d + 1 to the end (from index 4 to 8)
# Example : 1 5 8 4 1 3 4 6 7 -> this is the next permutation

def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)-1, 0, -1): #loops from right to left
        if nums[i] > nums[i-1]: # finding the first decreasing number from right to left 
            target = nums[i-1] #get 4 
            swap = i-1 # swap = 3
            while swap<len(nums)-1:
                if (nums[swap+1]) <= target:
                    break
                swap += 1
            nums[swap], nums[i-1] = nums[i-1], nums[swap] #swap the values
            nums[i:] = nums[i:][::-1] #reverse the list from i to the end 
            return
    
    nums.reverse()
    return

print(nextPermutation([1,2,3]))    