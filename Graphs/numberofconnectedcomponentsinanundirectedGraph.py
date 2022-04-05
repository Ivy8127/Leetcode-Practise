def countComponents(n, edges):
    par = [i for i in range(n)]
    rank = [1]*n

    def find(n1):
        res = n1
        while par[res] != res:
            #path compression
            par[res] = par[par[res]]
            res = par[res]
        return res

    def union(n1,n2):
        x =find(n1)
        y =find(n2) 

        #if they have the same parent, don't do anything
        if x == y:
            return 0 #we did not merge them
        #merge them if they have different root parents
        if rank[x] >= rank[y]:
            #make x the root parent
            par[y] = x
            rank[x] += rank[y]
        else: #y is the root parent
            par[x] = y 
            rank[y] += rank[x]
        return 1
    res = n #total no of components at the begining
    for n1,n2 in edges:
        res -= union(n1,n2) #decrement the result everytime there is a succesful union 
    return res #number of connected components 

print(countComponents(5,[[0,1],[1,2],[3,4]]))  #returns 2  
#par=[0,1,2,3,4] 
#[0,0,0,3,3]
# rank = [2,2,1,2,1]   #2

def countC(edges, n):
    rank = [1]* n
    par = [i for i in range(n)]

    def find(node):
        res = node
        while res != par[res]:
            par[res] = par[par[res]]
            res = par[res] 
        return res

    def union(node1, node2):
        x, y = find(node1), find(node2) 
        if x == y :
            return 0
        if rank[x] > rank[y]:
            par[y] = x
            rank[x] += rank[y]
        else:
            par[x] = y 
            rank[y] += rank[x]
        return 1
    res = n    
    for node1, node2 in edges:
        res -= union(node1,node2)
    return res
print(countC([[0,1],[1,2],[3,4]],5))  


def countcomps(edges,n):
    par = [i for i in range(n)]
    rank = [1] * n

    def find(node):
        while node != par[node]:
            par[node] = par[par[node]] #path compression
            node = par[node]
        return node

    def union(node1,node2):
        x = find(node1)
        y = find(node2)
        if x == y:
            return 0
        else:
            if rank[x] > rank[y]:
                par[y] = x
                rank[x] += rank[y]
            else:
                par[x] = y
                rank[y] += rank[x]
        return 1 
    res = n
    for n1,n2 in edges:
        res -= union(n1,n2) 

    return res
#print(countcomps([[0,1],[1,2],[3,4]],5)) 
def countcompz(n, edges):
    par = [i for i in range(n)]
    rank = [1]* n
    
    def find(node):
        res = node
        while res != par[res]:
            res = par[res]
        return res
    
    def union(n1,n2):
        x,y = find(n1), find(n2)
        if x == y:
            return 0
        else:
            if rank[x] > rank[y]:
                par[y] =x
                rank[x] += rank[y]
            else:
                par[x] =y
                rank[y] += rank[x]
        return 1
    count = 5
    for n1, n2 in edges:
        count -= union(n1,n2)
    return count  
print(countcompz(5,[[0,1],[1,2],[3,4]]))                                  





                   