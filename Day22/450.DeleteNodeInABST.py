"""
1. search for a node to remove
2. if the node is found, delete the node

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]

# need to reconstruct the tree if 
root.left and root.right both exsit
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def deleteNode(self,root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1, cannot found key
        if not root: 
            return root 
        # 2,3,4,5, found the key, and there are 4 situations 
        if root.val == key: 
            if not root.left and not root.right: 
                return None 
            elif not root.left: 
                return root.right 
            elif not root.right: 
                return root.left 
            else: 
                cur = root.right 
                while cur.left: 
                    cur = cur.left 
                cur.left = root.left 
            return root.right 
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key: 
            root.right = self.deleteNode(root.right, key) 
        return root 