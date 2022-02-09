#Not the optimal approach
from collections import defaultdict
def preferrredRestaurant(prefered_r):
    #create a hashmap
    hashmap = defaultdict(int)
    for i in range(len(prefered_r)):
        #key = len of row - idx of restaurant
        for j in range(len(prefered_r[i])):
           hashmap[prefered_r[i][j]] += len(prefered_r[i]) - prefered_r[i][j] + 1
    max_val = 0         
    for k,val in hashmap.items():
        if val > max_val:
            max_val = val
            return k 
    return -1                       

print(preferrredRestaurant([[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8],[2,3,4,5,6,7,8,1]]))        