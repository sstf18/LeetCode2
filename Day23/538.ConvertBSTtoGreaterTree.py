"""
this is BST, left < mid < right
changed to the original key plus the sum of all keys greater than the orignal key in BST


Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

"""

from typing import Optional


class TreeNode: 
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
        self.pre = 0 
        self.traversal(root)
        return root 
    def traversal(self, cur):
        if not cur: 
            return 
        self.traversal(cur.right)
        cur.val = cur.val + self.pre
        self.pre = cur.val
        self.traversal(cur.left)
