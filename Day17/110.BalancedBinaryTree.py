"""
given a bianry tree, determine if it is height-balanced

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def isBalanced(self, root: Optional[TreeNode])-> bool: 
        if self.get_height(root) != -1: 
            return True 
        else: 
            return False 
    def get_height(self, root: TreeNode) -> int: 
        if not root: 
            return 0 
        left_height = self.get_height(root.left)
        if left_height == -1: 
            return - 1
        
        right_height = self.get_height(root.right)
        if right_height == -1: 
            return - 1

        diff_height = abs(right_height - left_height)
        if diff_height > 1: 
            return -1 
        else: 
            return 1+max(left_height, right_height)
