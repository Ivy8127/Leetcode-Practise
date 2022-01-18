# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1,list2):
        dummy = ListNode()
        curr = dummy
        while list1 or list2:
            if list1 and not list2:
                next_val = list1.val
                list1 = list1.next
            elif list2 and not list1 :
                next_val = list2.val
                list2 = list2.next
            else:
                if list1.val <= list2.val:
                    next_val = list1.val
                    list1 = list1.next
                else:
                    next_val = list2.val
                    list2 = list2.next
            curr.next = ListNode(next_val)
            curr = curr.next
        return dummy.next

l1 = ListNode(1) 
l1.next = ListNode(2)  
l1.next.next = ListNode(4)  
l2 = ListNode(1)        
l2.next = ListNode(3)        
l2.next.next = ListNode(4) 
results = Solution().mergeTwoLists(l1,l2)  
print(results.val,results.next.val,results.next.next.val,results.next.next.next.val,results.next.next.next.next.val)     
        

