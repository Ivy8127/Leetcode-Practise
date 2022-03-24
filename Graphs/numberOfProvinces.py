class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.count = n
        self.rank = [1] * n
        
    def find(self,node):
        if self.parent[node] != node:
            return self.find(self.parent[node])
        return self.parent[node]
    
    def union(self,node1,node2):
        x,y = self.find(node1),self.find(node2)
        if x!=y:
            if self.rank[x] > self.rank[y]:
                self.parent[y] = x
                self.rank[x] += self.rank[y]
            else:
                self.parent[x] =y
                self.rank[y] += self.rank[x]               
            self.count -=1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        row = len(isConnected)
        col = len(isConnected[0])
        for r in range (row):
            for c in range(col):
                if isConnected[r][c] == 1:
                    uf.union(r,c)
        return uf.count            
        
        