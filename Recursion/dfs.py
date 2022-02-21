#Recusrive dfs algorithm
#to keep track of visited node
#Time complexity O(V+E)
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        #means it is unvisited
        visited.add(node)
        print(node)
        #visit all its adjacent nodes recursively
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph,'A') 