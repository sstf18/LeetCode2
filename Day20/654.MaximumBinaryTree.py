"""
given array "nums" with no duplicates. 
building maximum binary tree: 
1. root is the max of nums 
2. left subtree on the left side of max value
3. right subtree on the right of max value
"""

from typing import List, Optional


class TreeNode: 
    def __inin__(self, val=0, left=None, right=None): 
        self.val = val
        self.left = left 
        self.right = right 

class Solution: 
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1: 
            return TreeNode(nums[0])

        maxValue = 0 
        maxIdx = 0 
        node = TreeNode(0)
        # find the max value and the index of max value 
        for i in range(len(nums)):
            if nums[i] > maxValue: 
                maxValue = nums[i]
                maxIdx = i
        node.val = maxValue

        # left subtree 
        if maxIdx > 0: 
            new_list = sum[:maxIdx]
            node.left = self.constructMaximumBinaryTree(new_list)

        # right subtree 
        if maxIdx < len(sum) -1 : 
            new_list = sum[maxIdx+1:]
            node.right = self.constructMaximumBinaryTree(new_list)
        return node
