#classic preorer traversal
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
           #base cases
        if left =='' and right == '':
            return res
        elif left == '':
            res += "()" + "(" + right + ")"
        elif right =='':
            res += "(" + left + ")"
        else: #both left and right are not null
            res += "(" + left + ")"+ "(" + right + ")"
        return res    
            
        