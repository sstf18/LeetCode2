"""
Given a binary tree, 
find its minimum depth.

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class solution: 
    def minDepth(self,root: Optional[TreeNode])-> int: 
        return self.getDepth(root)
    def getDepth(self, node): 
        if not node: 
            return 0 
        leftHeight = self.getDepth(node.left)
        rightHeight = self.getDepth(node.right)

        if node.left == None and node.right != None: return rightHeight + 1 
        if node.left != None and node.right == None: return leftHeight + 1 
        result = 1+ min(leftHeight, rightHeight)
        return result
    