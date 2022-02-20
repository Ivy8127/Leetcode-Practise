#Approach
#draw a number line as you think about this problem and draw the arrays on the line
#sort the array first because the intervals are in ascending order
#The pattern is comparing the last value in the output array to the current start value in the current index
#if the start value is smaller than the the last value then they are overlapping intervals
#merge the 2 intervals by picking the maximum value between the current last and output last value
#otherwise add the array to the results
def merge_intervals(arr):
    #sort the intervals
    arr.sort()
    res = [arr[0]]  
    for i in range(1,len(arr)):
        lastEnd = res[-1][1] #would be 3
        if arr[i][0] <= lastEnd: #2  ... 2<3 therefore they overlap
            #merge the 2 intervals
            res[-1][1] = max(lastEnd,arr[i][1]) #max(3,6)
        else:
            res.append([arr[i][0],arr[i][1]]) 
    return res           

print(merge_intervals([[1,3],[8,10],[15,18],[2,6]]))   



def merge(intervals):
    intervals.sort()
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        end = res[-1][1]
        start = intervals[i][0]
        #compare start and end
        
        if start <= end: #they are overlappping
            #merge them
            res[-1][1] = max(end, intervals[i][1])
            
        else:
            res.append([start, intervals[i][1]])
            
    return res        
                