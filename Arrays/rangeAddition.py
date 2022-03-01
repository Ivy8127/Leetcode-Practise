def rangeAddition(length,updates):
    #create an empty array initialized to zeros
    res = [0] * length

    #go through every update
    for update in updates:
        start, stop, inc = update
        #assign to the new array at the position of start, increment the value 
        res[start] += inc
        if stop < length -1: #if we have not reached the end of the array
            #assign the value after end, decrement it by inc
            res[stop+1] -= inc
    for i in range(1, len(res)):
        res[i] = res[i] + res[i-1]
    return res
print(rangeAddition(5, [[1,3,2],[2,4,3],[0,2,-2]]))  


def wifiRouters(buildingCount, routerLocation, routerRange):
    n = len(buildingCount)
    routerCount = [0]*n
    
    for i in range(len(routerLocation)):
        rng = routerRange[i]
        startIdx = max(0, routerLocation[i]-1-rng)
        endIdx = min(n-1, routerLocation[i]-1+rng)
        
        routerCount[startIdx] += 1
        if endIdx < n-1:
            routerCount[endIdx+1] -= 1
    
    for i in range(1, n):
        routerCount[i] += routerCount[i-1]
    
    count = 0
    for i in range(n):
        if routerCount[i] >= buildingCount[i]:
            count += 1
    return count 
