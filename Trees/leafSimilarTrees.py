#Recursive dfs, appending leaf nodes to a list and comparing both lists called on the 2 root nodes
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res = []
        res2 = []
        self.similarLeaf(root1, res)
        self.similarLeaf(root2, res2)
        return res == res2
    
    def similarLeaf(self, root, output=[]):
        if not root:
            return
        #traverse to the leaf node
        if root.left == None and root.right == None:
            output.append(root.val)
        self.similarLeaf(root.left, output) 
        self.similarLeaf(root.right,output)    
            
        