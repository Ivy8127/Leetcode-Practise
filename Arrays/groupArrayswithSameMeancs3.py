#The idea is to find the mean of each array in the 2d array
#Then check if that mean is in a mean group/list
#if it is not, just append the index value to the result and proceed to add the
#mean to the mean list
#If it's there, this tells you that this a repetition of the mean, right?
#Just find the index of that mean in the mean list and append the current index of the matching mean to the group
def groupArrays(arr):
    #takes in a 2d array
    res = []
    mean = 0
    meanGroup = []
    for index , value in enumerate(arr):
        mean = sum(value)/len(value)
        if mean in meanGroup:
            res[meanGroup.index(mean)].append(index)
        else:
            res.append([index])  
        meanGroup.append(mean) 
    return res         
print(groupArrays([[3, 3, 4, 2],[4, 4],[4, 0, 3, 3],[2, 3],[3, 3, 3]]))            