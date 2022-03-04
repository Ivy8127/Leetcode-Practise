#Time complexity 0(n)
def isMonotonic2(arr):
  decreasing = True
  increasing = True
  for i in range(1,len(arr)):
    if arr[i-1] < arr[i]:  #eg 2 3 => increasing
      decreasing = False
    elif arr[i-1] > arr[i]:#eg 4 3 => decreasing
      increasing = False
  return increasing or decreasing    
print(isMonotonic2([6,5,5,4])) 


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if sorted(nums) == nums or sorted(nums, reverse=True)== nums:
            return True
        return False
        
        
