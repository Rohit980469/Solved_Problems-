from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        node = deque([root])
        while node:
            x = len(node)
            prev = None
            for i in range(x):
                curr = node.popleft()
                if prev :
                    prev.next = curr
                prev = curr
                if curr.left:
                    node.append(curr.left)
                if curr.right:
                    node.append(curr.right)
        return root