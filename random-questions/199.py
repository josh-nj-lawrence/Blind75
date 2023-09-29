from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Could BFS and append last element of each level to result
        if root is None:
            return []
        result = []
        queue = deque([root]) 
        
        while queue:
            curr = queue
            queue = deque()
            while curr:
                node = curr.popleft()
                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(node.val)
        return result
            