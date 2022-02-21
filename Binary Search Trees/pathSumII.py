#Uses path sum 1 to solve 
#21/02/2022
#32 mins
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = []
        res = []
        def dfs(node, currSum):
            if node is None:
                return []
            currSum += node.val
            stack.append(node.val)
            if node.left == None and node.right == None:
                if currSum == targetSum:
                    res.append(list(stack))      
            dfs(node.left, currSum) or dfs(node.right, currSum)
            stack.pop()      
        dfs(root,0)
        return res