"""
given a binary seach tree and a val, 
return the subtree with the node equals val
if such node does not exist, reutrn null. 

Input: 
root = [4,2,7,1,3], val = 2

Output: 
[2,1,3]
"""

from typing import Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def searchBST(self, root: Optional[TreeNode], val:int)-> Optional[TreeNode]:
        if not root or root.val == val: 
            return root 
        if val < root.val: 
            return self.searchBST(root.left, val)
        if val > root.val: 
            return self.searchBST(root.right, val)
        