#The approach is to calculate a prefix and postfix array
#Multiply the values of the prefix and postfix array and append to an output array
def productArray(nums):
    pre = 1
    post = 1
    answer = []
    prefix = [pre]
    postfix = [post]
    for i in range(1,len(nums)):
        pre = nums[i-1] * pre
        prefix.append(pre)
    for i in range(len(nums)-2,-1,-1):
        post = nums[i+1]* post
        postfix.insert(0,post)
    for i in range(len(prefix)):
        answer.append(prefix[i]* postfix[i])    
    return answer
print(productArray([1,2,3,4]))    #24, 12, 8, 8    
