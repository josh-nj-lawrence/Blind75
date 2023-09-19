# Start at 9:54 pm - 10:06 pm

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
            """
            :type root: Node
            :rtype: List[int]
            """
            stack, rst = [], []
            while stack or root:
                if root:
                    rst.append(root.val)
                    for c in root.children[:0:-1]:
                        stack.append(c)
                    if root.children:
                        tmp = root.children[0]
                        root.children = root.children[1:]
                        root = tmp
                    else:
                        root = None
                else:
                    root = stack.pop()
            return rst