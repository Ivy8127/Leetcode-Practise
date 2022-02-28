#Just reverse the list is all
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        q.append(root)
        while q:
            qlen = len(q)
            ans = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    ans.append(node.val)
                    if node.left != None:
                        q.append(node.left)
                    if node.right != None:    
                        q.append(node.right)
            if ans:    
                res.append(ans) 
                    
        return res[::-1]         
        
        