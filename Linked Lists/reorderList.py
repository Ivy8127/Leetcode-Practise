# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #Split the list into two halfs
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #Reverse the second half 
        #reverse a list
        second = slow.next
        prev = slow.next = None 
        #slow.next is None bc we're splitting our list into 2, so pointing the last pointer of the first half to None
        
        while second:
            node = second.next
            second.next = prev
            prev = second
            second = node
        #Merge the 2 lists
        first = head
        second = prev
        
        while second: #we can use any pointers but we know that the second half could be smaller than the first
            #create temp variables bc we will break the next
            temp1 , temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            #Shift pointers
            first = temp1
            second = temp2
            
        