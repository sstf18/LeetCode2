"""
Given a n-ary tree, find its maximum depth.

Input: root = [1,null,3,2,4,null,5,6]
Output: 3

"""

class Node: 
    def __init__(self, val=None, children=None):
        self.val = val 
        self.children = children 

class Solution: 
    def maxDepth(self, root: 'Node') -> int:
        return self.getDepth(root)
    def getDepth(self, node):
        if not node: 
            return 0 
        max_depth = 1 
        for child in node.children: 
            max_depth = max(max_depth, self.getDepth(child) + 1)
        return max_depth