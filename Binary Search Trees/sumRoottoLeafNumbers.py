#recursive dfs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], res = 0) -> int:
        if not root:
            return 0
        res = 10 * res + (root.val)
        if root.left == None and root.right == None:
            return res
        return self.sumNumbers(root.left, res) + self.sumNumbers(root.right, res)

            
        