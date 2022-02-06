#Time complexity O(n^2)
def uniquePaths(m, n):
    bottomRow = [1] * (n)
    for i in range(m-1):
        newRow = [1] * (n)
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + bottomRow[j]
        bottomRow = newRow
    return bottomRow[0]

print(uniquePaths(5,3))    