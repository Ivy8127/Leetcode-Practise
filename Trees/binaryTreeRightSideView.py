# Definition for a binary tree node.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = []
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            res.append(node.val)        
        return res             
        