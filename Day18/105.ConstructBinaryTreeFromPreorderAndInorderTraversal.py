"""
Given two integer arrays preorder and inorder where preorder is the preorder traversal of 
a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree. 

Input: 
preorder = [3,9,20,15,7], (middle, left, right)
inorder = [9,3,15,20,7], (left, middle, right)

Output: 
[3,9,20,null,null,15,7]

"""

from typing import List, Optional


class TreeNode: 
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def buildTree(self, preorder:List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: 
            return None 
        
        root_val = preorder[0]
        root = TreeNode(root_val)

        separator_idx = inorder.index(root_val)

        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1:]

        preorder_left = preorder[1: 1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]

        root.left = self.buildTree(inorder_left, preorder_left)
        root.right = self.buildTree(inorder_right, preorder_right)

        return root 