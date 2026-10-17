from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        par_dict = {}
        special_node = None
        def parent(node, par):
            nonlocal special_node
            if not node :
                return
            par_dict[node] = par
            if node.val == start:
                special_node = node
            parent(node.left, node)
            parent(node.right, node)
        parent(root,None)

        nodes = deque([(special_node, 0)])
        visited = {special_node}
        ans = 0
        while nodes:
            curr , dis = nodes.popleft()
            ans = dis
            for x in (curr.left, curr.right, par_dict[curr]):
                if x and x not in visited:
                    visited.add(x)
                    nodes.append((x,dis+1))

        return ans