"""
transfer sorted array to BST

1. find the mid
2. set the mid as root, then traversal root.left and root.right
3. return root 

"""

from typing import List, Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution: 
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.traversal(nums, 0, len(nums)-1)
        return root 

    def traversal(self, nums, left, right):
        if left > right: 
            return None 
        mid = left + (right - left) // 2 
        root = TreeNode(nums[mid])
        root.left = self.traversal(nums, left, mid-1 )
        root.right = self.traversal(nums, mid+1, right)
        return root 

