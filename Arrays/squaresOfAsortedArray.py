def squares(nums):
    res = []
    for num in nums:
        num = num * num
        res.append(num)
    res.sort()
    return res
print(squares([-7,-3,2,3,11]))        

#More efficient linear time sln
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #come up with a linear time solution
        #using a 2 pointer technique
        squares = [0] * len(nums)
        lstIdx = len(squares) -1
        start = 0
        end = len(nums)-1
        while start <= end:
            left = nums[start] * nums[start]
            right = nums[end] * nums[end]
            if left > right:
                squares[lstIdx] = left
                start +=1
            else:
                squares[lstIdx] = right
                end -= 1
            lstIdx -= 1
        return squares  
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
       #49 9 4 9 121
       #    4 9  9  49 121 
        squares = [0]* len(nums)
        start , end = 0 , len(nums)-1
        lst = len(nums)-1 
        while start <= end:
            left, right = nums[start] ** 2 , nums[end]**2
            if left > right:
                squares[lst] = left
                start +=1
            else:
                squares[lst] = right
                end-=1
            lst -=1
        return squares    
                  
       