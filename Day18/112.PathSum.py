"""
given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that 
adding up all the values up all the values along the path
equals targetSum 


Input: 
root = [5,4,8,11,null,13,4,7,2,null,null,null,1],
targetSum = 22

Output: 
true

Explanation: 
The root-to-leaf path with the target sum is shown.
"""
from typing import Optional


class TreeNode: 
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right 

class Solution: 
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int)->bool: 
       if not root: return False 
       return self.traversal(root, targetSum - root.val)

    def traversal(self, cur: TreeNode, count: int):
        if not cur.left and not cur.right and count == 0: 
            return True 
        if not cur.left and not cur.right and count != 0: 
            return False 
        # left 
        if cur.left: 
            count -= cur.left.val 
            if self.traversal(cur.left, count):
                return True 
            count += cur.left.val
        # right
        if cur.right: 
            count -= cur.right.val 
            if self.traversal(cur.right, count):
                return True 
            count += cur.right.val
        return False 

