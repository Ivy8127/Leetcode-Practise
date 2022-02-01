#Approach 1 - bruteforce solution, find every possible sub array's product O(n^2)=inefficient
def maxProduct(nums):
    if len(nums) == 0:
        return 0
 
    result = nums[0]
 
    for i in range(len(nums)):
        accu = 1
        for j in range(i, len(nums)):
            accu *= nums[j]
            result = max(result, accu)
 
    return result

#print(maxProduct([2,3,-2,4])) 


#Approach 2 Modified Kadane's algorithm
def maxP(nums):
    if len(nums) == 0 :
        return 0
    if len(nums) == 1:
        return nums[0]
    currP = 1
    max_P = 0
    #forward pass
    for i in range(len(nums)):
        currP *= nums[i]
        max_P = max(max_P, currP)
        if currP == 0:
            currP = 1
    #backward pass        
    currP = 1
    for i in range(len(nums)-1, -1,-1):
        currP *= nums[i]
        max_P = max(currP, max_P)
        if currP == 0:
            currP = 1

    return max_P    

print(maxProduct([2,0,-3,6]))        
