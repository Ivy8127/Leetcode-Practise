class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end
class Solution:
    def canAttendMeetings(self,intervals):
        if len(intervals) == 0:
            return True
        #sort in ascending order
        intervals.sort(key = lambda x : x.start)
        for i in range(1,len(intervals)):
            #find overlapping intervals
            if intervals[i].start < intervals[i-1].end:
                #they overlap therefore they can't attend all meetings
                return False
        return True
#Time -> 0nlogn
#Space -> o(1)
def canAttendMeetings(intervals):
    intervals.sort(key = lambda x: x[0])
    #he can attend all meetings if there is no overlapping meetings
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True 

def canAttendMeetings(intervals):
    intervals.sort() 
    for i in range(1,len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True    