#Approach on Notion
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix)-1
        
        while left < right :
            for i in range(right - left):
                top, bottom = left, right
                #create a temp variable
                topleft = matrix[top][left+i]
                
                #move the bottom left to top left
                matrix[top][left + i] = matrix[bottom -i][left]
                
                #move the value at the bottom right to the value at the bottom left
                matrix[bottom - i][left] = matrix[bottom][right -i]
                
                #move value at top right to value at bottom right
                matrix[bottom][right -i] = matrix[top+i][right]
                
                #move value at top left to top right
                matrix[top+i][right] = topleft
            right -=1
            left+=1
            
            
        