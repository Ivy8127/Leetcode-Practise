class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    dummy = ListNode()
    curr = dummy
    def mergeKlist(lists):
    heap =[]
    for i in lists:
        while i!= None:
            heappush(heap,i.val)
            i = i.next
    print(heap) 

    while len(heap) > 0:
        #pop the minimum value from the heap and 
        #insert it into the new linked list
        curr.next = ListNode(heappop(heap))
        #Traverse to the next node
        curr = curr.next
    return dummy.next  #return the head of the linked list          

      

print(mergeKlist([[1,4,5],[1,3,4],[2,6]])) 

#Time complexity O(nlogk) 
#more efficient that divide and conquer approach