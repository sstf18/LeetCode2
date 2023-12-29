"""
Example 1: 
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

"""

import collections
from typing import List, Optional

class TreeNode: 
    def __init__(self, val=0, left=None, right = None) :
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        if not root: 
            return []

        queue = collections.deque([root])
        result = []
        while queue: 
            level = []
            for _ in range(len(queue)): 
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
            result.append(level)
        return result 