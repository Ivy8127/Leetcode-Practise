class TreeNode:
    def __init__(self,val=0,left = None, right = Node):
        self.right = right
        self.val = val
        self.left = left

class Sln:
    def boundaryofBtree(self,root):
        def leftbfs(node):
            if node:
                if node.left == None and node.right == None:
                    return []
                else:
                    if node.left:
                        return [node.val] + leftbfs(node.left)
                    else:
                        return [node.val] + leftbfs(node.right)        
            else:
                return [] 

        def rightbfs(node):
            if node:
                if node.left == None and node.right == None:
                    return []
                else:
                    if node.right:
                        return [node.val] + rightbfs(node.right)
                    else:
                        return [node.val] + rightbfs(node.left)        
            else:
                return []    
        def findLeaves(node):
            if node:
                if node.left == None and node.right == None:
                    return [node.val]
                else:
                    return findLeaves(node.left)  + findLeaves(node.right)  
            else:
                return []    

        return [root.val] + leftbfs(root.left) + findLeaves(root.left) + findLeaves(root.right) + rightbfs(root.right)

        