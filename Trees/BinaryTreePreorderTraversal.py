class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        def preorder_traversal(root):
            if root:
                preorder.append(root.val)
                preorder_traversal(root.left)
                preorder_traversal(root.right)
        preorder_traversal(root)
        return preorder