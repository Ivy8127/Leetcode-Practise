#This is constant time and O(n) space
class Solution:
    from collections import Counter
    def majorityElement(self, nums: List[int]) -> int:
        majorElement = Counter(nums)
        for k, v in majorElement.items():
            if v > (len(nums)//2):
                return k
            
#can i do this in linear time and constant space?        