# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Create a dummy node who's next pointer is the head
        dummy = ListNode(0, head)
        #set the left pointer to start at the dummy node
        left = dummy
        right = head
        #change the position of the right pointer to position of head + n
        while right and n>0:
            right = right.next
            n-=1
       #shift the left and right till the right becomes null 
    #this gets the value whose next pointer we want to delete (left ptr)
        while right:
            left = left.next
            right = right.next
        #delete the node
        
        left.next = left.next.next
        
        return dummy.next # bc dummy.next is the head of the ll (not returning dummy)
            
        
                
                
                
                
        