"""
given BST, find the minimum absolute difference
in any two nodes in the tree

Input: root = [1,0,48,null,null,12,49]
Output: 1
"""

from typing import Optional


class TreeNode: 
    def __init__(self, val=0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def __init__(self):
        self.result = float('inf')
        self.pre = None 
    def traversal(self, cur):
        if not cur: 
            return 
        # left 
        self.traversal(cur.left)
        # middle 
        if self.pre: 
            self.result = min(self.result, cur.val - self.pre.val ) # since the cur always bigger than pre
        self.pre = cur # let the pre->cur, which means it moves forward 
        # right
        self.traversal(cur.right)

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.traversal(root)
        return self.result


