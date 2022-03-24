class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = {i:[] for i in range(numCourses)}
        #crsMap ={0:[],1:[] }
        for crs,pre in prerequisites:
            crsMap[crs].append(pre) # {0:[],1:[0]}
        visited = set()    
        def dfs(crs):
            #dfs(1)
            #base case
            if crsMap[crs] == []: #bc it means that this course contains no prereq hence can be finished
                return True
            if crs in visited: #bc it this course has already been visited causing a loop therefore cant be finished
                return False
            
            visited.add(crs)
            for pre in crsMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)  
            crsMap[crs] = []
            return True 
        #we loop through the entire course bc think of a graph where they are not connected
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True    
            
        
