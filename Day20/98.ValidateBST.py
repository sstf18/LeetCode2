"""
check if a tree is BST

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

from typing import Optional


class TreeNode: 
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def __init__(self):
        self.pre = None 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # is root is empty, it shuold be BST
        if root is None: 
            return True 

        # check the left side 
        left = self.isValidBST(root.left)

        # middle, pre is the previous node of root
        if self.pre and self.pre.val >= root.val: 
            return False 
        self.pre = root 

        # right check 
        right = self.isValidBST(root.right)
        return left and right 
        