class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #using bfs
        queue = deque()
        fresh, time = 0,0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                #going through evry cell in grid
                if grid[row][col] == 1:
                    fresh+=1
                if grid[row][col] == 2:
                    queue.append([row,col])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]            
        while queue and fresh > 0:
            #pop values from queue
            for i in range(len(queue)):
                row, col = queue.popleft()
                #check all directions for every single queue coordinate
                for dr,dc in directions:
                    r ,c = dr + row, dc + col
                    #check if out of bounds, if true, continue
                    if(r < 0 or r == len(grid) or 
                       c < 0 or c == len(grid[0])or
                       grid[r][c] != 1):
                        continue
                    #else mark the fresh orange as rotten    
                    grid[r][c]= 2 
                    #append to queue
                    queue.append([r,c])   
                    fresh -=1
            time+=1
        return time if fresh == 0 else -1


