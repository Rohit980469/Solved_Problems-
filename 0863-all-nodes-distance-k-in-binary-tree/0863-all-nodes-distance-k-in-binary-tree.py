from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        par_dict = {}
        def par_link(node, par):
            if node is None:
                return 
            par_dict[node] = par
            par_link(node.left, node)
            par_link(node.right, node)
        par_link(root, None)

        node = deque([(target,0)])
        visited = {target}
        result = []
        while node :
            curr , dis = node.popleft()
            if dis == k:
                result.append(curr.val)
                continue
            for x in (curr.left, curr.right, par_dict[curr]):
                if x and x not in visited:
                    visited.add(x)
                    node.append((x,dis + 1))

        return result