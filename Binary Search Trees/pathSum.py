
#21/02/2022
#60 mins
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        if targetSum == root.val and root.left == None and root.right == None:
            return True
        
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

#More intuitive solution for me
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if node is None:
                return False
            currSum += node.val
            if node.left == None and node.right == None:
                if currSum == targetSum:
                    return True
                else:
                    return False
                
            return (dfs(node.left, currSum) or dfs(node.right, currSum)) 
        
        return dfs(root,0)
                    