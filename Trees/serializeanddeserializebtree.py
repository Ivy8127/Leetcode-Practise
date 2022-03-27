# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#Preorder traversals at their best
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def preorder(root):
            if root:
                res.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
            else:
                res.append("N")
                return
        preorder(root)
        return ','.join(res)                

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        self.index = 0
        values = data.split(",")
        
        def dfs():
            #base case
            if values[self.index] == "N":
                self.index +=1
                return None
            #convert to node
            node = TreeNode(int(values[self.index])) #convert to int
            self.index +=1
            node.left = dfs()
            node.right = dfs()
            return node #return root node
        return dfs()
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
tree = ser.serialize(root)
ans = deser.deserialize(tree)
print(ans)