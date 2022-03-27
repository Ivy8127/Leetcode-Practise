#An recursive dfs approach
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #base case 
        if not root:
            return 0
        
        elif root.val <= high and root.val >= low: #within range
            #traverse both it's right and left subtrees
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right, low,high)
        elif root.val < low: #left children nodes will be smaller bc its a bst so traverse to the right
            return self.rangeSumBST(root.right, low,high)
        elif root.val > high: #right children nodes will be higher so traverse to it's left subtree
            return self.rangeSumBST(root.left, low,high)
            

        
        