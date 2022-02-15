# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head == None:
            return None
        if head.next == None:
            return TreeNode(head.val)
        slow ,fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None
        root = TreeNode(middle.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(middle.next)
        return root