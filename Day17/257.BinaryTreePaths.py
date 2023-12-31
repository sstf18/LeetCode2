"""
Given the root of a binary tree, 
return all root-to-leaf paths in any order.
A leaf is a node with no children.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""

# Definition for a binary tree node.
from typing import List, Optional
class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 
class Solution: 
    def binaryTreePaths(self, root: Optional[TreeNode]) ->List[str]:
        path = []
        result = []
        # if not root: no more root
        if not root: 
            return result 
        # has root, traversal
        self.traversal(root, path, result)
        return result

    def traversal(self, cur, path, result): 
        
        #middle
        path.append(cur.val)
        if not cur.left and not cur.right: 
            sPath = '->'.join(map(str,path))
            result.append(sPath)

        #left 
        if cur.left: 
            self.traversal(cur.left, path, result)
            path.pop()

        #right
        if cur.right: 
            self.traversal(cur.right, path, result)
            path.pop()
        

