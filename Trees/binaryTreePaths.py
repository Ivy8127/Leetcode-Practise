
#using dfs to find paths joining them into strings connected by ->
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        return self.dfs(root,'')
    def dfs(self,root,path):
        if not root:
            return []
        path +=str(root.val)
        if root.left == None and root.right == None:
            return [path] 
        path += '->'
        return self.dfs(root.left,path) + self.dfs(root.right,path)
        
        