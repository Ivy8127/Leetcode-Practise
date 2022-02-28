from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #perform a bfs
        queue = deque()
        ans = []
        queue.append(root)
        
        while queue:
            level = []
            q_len = len(queue)
            for i in range(q_len):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
            if level:            
                ans.append(level)
        return ans