#Applies the same concept as a dfs
#Only difference is that it uses a queue, a FIFO structure
#Add a node to a queue
#Add all it's children nodes to a queue and visited list if they have not been visited, mark them as visited
#Pop the first node from the queue,if all children nodes are done
#Repeat till queue is empty

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}
visited = []
queue = []
def bfs(node, visited, graph):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        print(s)
        for children in graph[s]:
            if children not in visited:
                visited.append(children)
                queue.append(children)

print(bfs('A', visited, graph))