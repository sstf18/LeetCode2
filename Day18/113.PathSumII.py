"""
given the root of a binary tree and an integer targetSum
return all the root-to-leaf paths where the sum of the node values is targetSum 

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
"""

from typing import List, Optional


class TreeNode: 
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def __init__(self): 
        self.path = []
        self.result = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) ->List[List[int]]:
        if not root: 
            return self.result
        self.path.append(root.val)
        self.traversal(root, targetSum - root.val)
        return self.result
    
    def traversal(self, cur, count):
        if not cur.left and not cur.right and count == 0: 
            self.result.append(self.path[:])
        if not cur.left and not cur.right and count != 0: 
            return 
        if cur.left: 
            self.path.append(cur.left.val)
            count -= cur.left.val 
            self.traversal(cur.left, count)
            count += cur.left.val 
            self.path.pop()
        if cur.right: 
            self.path.append(cur.right.val)
            count -= cur.right.val 
            self.traversal(cur.right, count)
            count += cur.right.val 
            self.path.pop()
        return 
