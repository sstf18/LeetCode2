# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Collection, List, Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []
        queue = Collection.deque([root])
        right_view = []
        while queue: 
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1 :
                    right_view.append(node.val)
                if node.left: 
                    queue.append(node.left) 
                if node.right: 
                    queue.append(node.right)
        return right_view