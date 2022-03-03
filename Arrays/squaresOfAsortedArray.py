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
       