"""
Given the root of a binary tree, 
invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

"""

# Definition for a binary tree node.
from typing import Collection, Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
"""
class Solution: 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        if not root: 
            return None 
        
        root.left, root.right = root.right, root.left 
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root 


"""
class Solution: 
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        if not root: 
            return None 
        
        queue = Collection.deque([root])
        while queue: 
            for i in range(len(queue)):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root