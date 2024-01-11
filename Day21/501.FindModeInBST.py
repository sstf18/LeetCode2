"""
mode(s):most freeuently occurred element
for example: 1,2,2,2,2,4,5; 2 is the mode. 
in mathmatices, there are multiple modes in a list of numbers
"""

from typing import List, Optional


class TreeNode: 
    def __init__(self, val=0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def __init__(self): 
        self.result = []
        self.pre = None
        self.count = 0 
        self.maxCount = float('-inf')

    def traversal(self, cur): 
        if not cur: 
            return 
        # left 
        self.traversal(cur.left)
        # mid
        if self.pre and self.pre.val == cur.val: 
            count += 1 
        else: 
            count = 1 
        self.pre = cur
        if self.count == self.maxCount: 
            self.result.append(cur.val)
        if self.count > self.maxCount: 
            self.maxCount = self.count 
            self.result.clear()
            self.result.append(cur.val)
        # right 
        self.traversal(cur.right)


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.traversal(root)
        return self.result 