"""
given the root of a bST, and lowest and highest boundaries
as "low" and "high", [low, high]


Input: 
root = [1,0,2], low = 1, high = 2

Output: 
[1,null,2]
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root: 
            return None 
        # when the root is less than lowest boundries, then check the root.right
        if root.val < low: 
            right = self.trimBST(root.right, low, high)
            return right
        # when the root is bigger than highest boundries, then check the root.left
        if root.val > high: 
            left = self.trimBST(root.left, low, high)
            return left 
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root 