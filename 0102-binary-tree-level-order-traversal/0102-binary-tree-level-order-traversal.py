from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        curr =  Queue()
        curr.put(root)
        result  = []
        while not curr.empty():
            level = []
            for i in range(curr.qsize()):
                node = curr.get()
                level.append(node.val)
                if node.left != None:
                    curr.put(node.left)
                if node.right != None:
                    curr.put(node.right)
                
            result.append(level)
        return result