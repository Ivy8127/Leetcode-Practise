#Topological sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = {i:[] for i in range(numCourses)}
        #crsMap ={0:[],1:[] }
        for crs,pre in prerequisites:
            crsMap[crs].append(pre) # {0:[],1:[0]}
        visited = set() 
        cycle = set()
        res = []
        def dfs(crs):
            #base case
            if crs in visited: 
                return True
            if crs in cycle: 
                return False
            cycle.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs) #bc we want to iterate over a new empty set on the next iteration of the dfs call
            visited.add(crs)
            res.append(crs)
            return True 
        #we loop through the entire course bc think of a graph where they are not connected
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res  
        