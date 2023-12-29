"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

"""
import collections
from typing import Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
"""
class Solution: 
    def maxDepth(self, root: Optional[TreeNode])-> int: 
        if not root: 
            return 0 
        depth = 0 
        queue = collections.deque([root])

        while queue: 
            depth += 1 
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
        return depth
"""

class solution: 
    def maxdepth(self, root: TreeNode) -> int: 
        return self.getDepth(root)

    def getDepth(self, node):
        if not node: 
            return 0 

        leftheight = self.getDepth(node.left)
        rightheight = self.getDepth(node.right)
        height = 1 + max(leftheight, rightheight)
        return height 
 
        
        