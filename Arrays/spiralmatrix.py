#Approach 
#Time complexity O(m*n)
#space complexity O(1) 
def spiral_matrix(matrix):
    output = []
    #initialize 4 pointers
    left, right = 0 , len(matrix[0])
    top , bottom = 0 , len(matrix)
    while left < right and top < bottom:
        #get values in the top row
        for i in range(left, right):
            output.append(matrix[top][i])
        top +=1
        #get values in the right most column
        for i in range(top, bottom):
            output.append(matrix[i][right-1])
        right -=1
        #essentially if right and left or top and bottom pointers meet, the algorithm is done
        if not (left < right and top < bottom):
            break
        #get values from the bottom row
        for i in range(right -1,left-1,-1):
            output.append(matrix[bottom -1 ][i])
        bottom -=1 
        #get values from the left column   
        for i in range(bottom -1 , top -1,-1):
            output.append(matrix[i][left]) 
        #start again from left pointer    
        left +=1       
    return output 
print(spiral_matrix([[1,2,3],[4,5,6],[7,8,9]]))              