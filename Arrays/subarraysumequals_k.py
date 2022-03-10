#brute force sln but slow - brings tle on leetcode
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            currsum = 0
            for j in range(i, len(nums)):
                currsum += nums[j]
                if currsum == k:
                    count+=1
        return count 

#optimal O(n) time and space sln
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        count = 0
        currsum = 0
        for i in range(len(nums)):
            currsum+= nums[i]
            if currsum - k in hashmap:
                count += hashmap[currsum-k]
            if currsum in hashmap:
                hashmap[currsum] +=1
            else:
                hashmap[currsum] = 1
        return count         
            
            
        
                
        