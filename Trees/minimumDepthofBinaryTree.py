# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Typical recursive dfs :)
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        elif root.left == None or root.right == None: #edge case for a skewed tree
            return 1+ max(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))