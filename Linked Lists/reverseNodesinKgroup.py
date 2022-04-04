# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.findKth(groupPrev, k)
            if not kth:
                break
            #reverse the group
            prev , curr = kth.next, groupPrev.next
            groupNext = kth.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            #make the previous pointer point to the new reversed node
            #update psn of the prev node
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next    
            
    def findKth(self,curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr    
        