#Detailed approach on Notion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preOrder(root):
            if root:
                left = preOrder(root.left)
                right = preOrder(root.right)
            else:
                return None
            if left:
                left.right = root.right
                root.right = root.left
                root.left = None
                
            last = right or left or root
            return last
        
        preOrder(root)
        
        