class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r < 0 or r >= rows or c <0 or c >= cols or board[r][c] != word[i] or (r,c) in visited):
                return False
            visited.add((r,c))
            res = dfs(r +1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1) or dfs(r, c+1, i+1)
            visited.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0) : return True
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        rows = len(board)
        cols = len(board[0])     
        def dfs(i,j,idx):
            if idx == len(word):
                return True
            
            if ((i,j) in visited or i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[idx]):
                return False
            
            visited.add((i,j))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            for dr,dc in directions:
                if dfs(dr+i, dc + j, idx+1):
                    return True
            visited.remove((i,j))    
            return False   
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False            
                