# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], res=0) -> int:
        #perform a dfs recursively on the binary tree
        #reaching a leaf node is when the left and right subree are None
        #how do you convert binary to numbers in code
        if not root:
            return 0
        res = res * 2 + root.val
        if root.left == None and root.right == None:
            return res
            
        return self.sumRootToLeaf(root.left, res) + self.sumRootToLeaf(root.right, res)
        
        