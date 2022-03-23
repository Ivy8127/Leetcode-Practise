#Return the minimum number of conference rooms required
#Greedy method
#Time complexity 0(nlogn)
#Space  0(n)
class Intervals:
    def __init__(self,start,end):
        self.start = start
        self.end = end
class Sln:        
    def min_meeting_rooms(self,intervals):
        #create 2 sorted arrays of the start and end time
        start = sorted([i.start for i in intervals]) # 2 7  
        end = sorted([i.end for i in intervals]) # 4 10
        #2 pointer technique
        s,e = 0,0
        count, max_count = 0,0
        while s < len(intervals):
            if start[s] < end[e]:
                count+=1
                s+=1  
            else:
                count-=1
                e +=1
            max_count = max(count, max_count)
        return max_count             
print(min_meeting_rooms([[7,10],[2,4]])) #1 meeting room      
print(min_meeting_rooms([[0,30],[5,10],[15,20]]))   #2 meeting rooms         
print(min_meeting_rooms([[0,30],[5,10],[10,15]]))   #2 meeting rooms         
