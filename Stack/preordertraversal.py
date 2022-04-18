#binary tree iterative preorder traversal

class TreeNode:
    def __init__(self,val, left = None, right = None):
        self.left = left
        self.right = right
        self.val = val

    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = TreeNode(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = TreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
 

    def iterative_preorder(root):
        res = []
        stack = []
        if root is None:
            return 
        stack.append(root)
        while (len(stack)>0):
            node = stack.pop()
            res.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)      
        return res
root = TreeNode(1) 
elements = [2,3,4]
for e in elements:
    root.insert(e)
print(root.iterative_preorder())
  