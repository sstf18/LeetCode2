"""
given the root node of BST, and a value to insert into the tree

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

"""

from typing import Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # step 2 
        if not root: # found the location 
            return TreeNode(val)
        # step3 
        if root.val > val: 
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val: 
            root.right = self.insertIntoBST(root.right, val)
        return root