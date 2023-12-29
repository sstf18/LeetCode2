"""
Input: root = [1,2,3,4,5,6]
Output: 6

"""
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#solution 1

# class Solution: 
#     def countNodes(self, root: Optional[TreeNode]) -> int: 
#         return self.getNumber(root)

#     def getNumber(self, node):
#         if not node: 
#             return 0 
#         leftNumber = self.getNumber(node.left)
#         rightNumber = self.getNumber(node.right)
#         result = leftNumber + rightNumber + 1 
#         return result 

#solution 2

class Solution: 
    def countNodes(self, root: Optional[TreeNode])-> int:
        if not root: 
            return 0 
        # pointers 
        left = root.left 
        right = root.right 
        leftDepth = 0 
        rightDepth = 0 

        # get the depth of left 
        while left: 
            leftDepth += 1 
            left = left.left 
        # get the depth of right 
        while right: 
            rightDepth += 1 
            right = right.right 
        # if "==", means they are full binary tree , directly return 
        if leftDepth == rightDepth: 
            return (2 << leftDepth) - 1 

        # recursion : left, right , middle 
        leftCount = self.countNodes(root.left)
        rightCount = self.countNodes(root.right)
        result = leftCount + rightCount + 1 
        return result 


