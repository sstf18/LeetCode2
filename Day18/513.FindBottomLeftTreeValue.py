"""
Given the root of a binary tree, 
return the leftmost value in the last row of the tree.

Input: root = [2,1,3]
Output: 1

Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def findBottomLeftValue(self, root:Optional[TreeNode]) -> int: 
        self.max_depth = float('-inf')
        self.result = 0 
        self.traversal(root, 0)
        return self.result

    def traversal(self, node, depth):
        if node.left == None and node.right == None: 
            if depth > self.max_depth: 
                self.max_depth = depth 
                self.result = node.val 
        if node.left: 
            depth += 1 
            self.traversal(node.left, depth )
            depth -= 1
        if node.right: 
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1
