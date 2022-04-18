class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def iterative_inorder(root):
        stack, res = [],[]
        while True:
            if root != None:
                stack.append(root)
                root = root.left
            elif stack: #stack is not empty and root is null, then pop
                root = stack.pop()
                res.append(root.val) 
                root = root.right
            else: #is tack is empty, stop
                break
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(root.iterative_inorder())    


