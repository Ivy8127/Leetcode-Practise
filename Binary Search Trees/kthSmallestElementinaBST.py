class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #perform an inorder traversal
        #return the kth smallest value from the list created
        res = []
        def inorder(root): #left root right
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res[k-1]
            
            
        