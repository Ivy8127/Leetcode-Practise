# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) + self.pathSum2(root, targetSum)
    
    def pathSum2(self, node, summ):
        if not node:
            return 0
        count = 0
        if node.val == summ:
            count = 1
        newSum = summ - node.val
        count += self.pathSum2(node.left, newSum)
        count += self.pathSum2(node.right, newSum)
        
        return count
        
            
        
        
        