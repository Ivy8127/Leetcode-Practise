def setZeroes(matrix):
    out = []
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if matrix[i][k] == 0:
                out.append([i,k])
    for item in out:
        print(item) # 
        for a in range(len(matrix[item[0]])):
            matrix[item[0]][a] = 0
        for b in range(len(matrix)):
            matrix[b][item[1]] = 0
            
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))    