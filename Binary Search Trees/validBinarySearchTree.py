# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Using dfs to solve this, basically a recursion problem
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #using left and right boundaries to determine a valid bst
        
        def valid(node, left, right):
            if not node:
                return True #bc an empty node is a valid bst
            
            #the node value should be greater than the left subtree and less than the right subtree to be a valid bst
            if not (node.val > left and node.val < right):
                return False
            
            return (valid(node.left, left, node.val) and valid(node.right, node.val,right))
        
        return valid(root, float('-inf'), float('inf'))
        
        