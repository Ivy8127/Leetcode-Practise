class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            q = deque()
            q.append([r,c])
            visited.add((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    row = dr + r
                    col = dc+c
                    if (row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row,col) not in visited):
                        q.append([row,col])
                        visited.add((row,col))
                
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands 


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows= len(grid) 
        cols =len(grid[0])
        visited = set()
        def dfs(i,j):
            if (i,j) not in visited and i in range(rows) and j in range(cols) and grid[i][j] =="1":
                visited.add((i,j))
            else:
                return
            neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dr, dc in neighbors:
                dfs(dr+i, dc + j)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "0":
                    continue
                if (r,c) not in visited:
                    islands +=1
                    dfs(r,c)
        return islands                               