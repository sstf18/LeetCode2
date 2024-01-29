"""
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

from typing import Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
    
class Solution: 
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        # first 3 check that left and right is not empty
        if left == None and right != None: return False
        elif left != None and right == None: return False 
        elif left != None and right != None: return True 
        # check left and right's val is correct 
        elif left.val != right.val: return False 
        
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside 
        return isSame