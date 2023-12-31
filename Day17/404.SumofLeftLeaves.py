"""
Given the root of a binary tree, 
return the sum of all left leaves.

A leaf is a node with no children. 
A left leaf is a leaf that is the left child of another node.

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, 
with values 9 and 15 respectively.
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.getLeftLeaves(root)
    def getLeftLeaves(self, root):
        if not root: 
            return 0 
        leftValue = self.getLeftLeaves(root.left)
        if root.left and not root.left.left and not root.left.right: 
            leftValue = root.left.val
        rightValue = self.getLeftLeaves(root.right)

        sum = leftValue + rightValue
        return sum 