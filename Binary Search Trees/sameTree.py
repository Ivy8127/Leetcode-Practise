# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base cases
        #1. If both p and q are null
        if not p and not q:
            return True
        #2. If p is null and q is not null or p is not null and q is null
        #3. if the value of p is not equal to the value of q =>false
        if not p or not q or p.val != q.val:
            return False
        
        #both the right and the left subtree need to be True for it to be the same tree
        return (self.isSameTree(p.left, q.left) and
         self.isSameTree(p.right, q.right))
        