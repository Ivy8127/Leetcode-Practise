#Brute force approach O(n^2)
#find the minimum height bc a maximum height will lead to water overflow
#find the max area by multiplying the min height by the distance between the 2 pointers
import numpy as np
def maxWater(height):
    maximum = -np.inf
    for i in range(len(height)):
        for j in range(i+1, len(height)):
            minimum = min(height[i],height[j])
            maximum = max(maximum, minimum * (j-i))
    return maximum 

#Most efficient sln.
#Linear time solution using 2 pointer technique -O(n)   
def maxArea(height):
    maxi = 0
    left = 0
    right = len(height)-1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        maxi = max(maxi,area)
        if height[left] < height[right]:
            left += 1
        else:
            right -=1
    return maxi                          
print(maxArea([1,8,6,2,5,4,8,3,7]))    #49