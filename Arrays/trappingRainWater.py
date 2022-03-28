class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0]* len(height)
        maxRight = [0] * len(height)
        maxx = 0
        for i in range(1,len(height)):
            maxx= max(height[i-1],maxx)
            maxLeft[i] = maxx
            
        maxx= 0
        for i in range(len(height)-2,-1,-1):
            maxx= max(height[i+1],maxx)
            maxRight[i] = maxx
        
        res = 0
        for i in range(len(height)):
            temp = min(maxLeft[i],maxRight[i]) - height[i]
            if temp > 0:
                res+= temp
            else:
                continue
        return res
