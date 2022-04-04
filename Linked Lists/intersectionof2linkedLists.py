#The optimal sln linear time and constant space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1,l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


#non optimal sln - using a hashmap therefore, linear space complexity

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = {}
        curr = headA
        while curr != None:
            visited[curr] = 1
            curr = curr.next
        
        curr = headB
        
        while curr != None:
            if curr in visited:
                return curr
            curr = curr.next
            
        return None