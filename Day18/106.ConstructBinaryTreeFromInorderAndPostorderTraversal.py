"""
Given two integer arrays "inorder" and "postorder", where "inorder" is 
the inorder traversal of a binary tree and postorder is the postorder traversal
of the same tree, construct and return the binary tree. 

Input: 
inorder = [9,3,15,20,7], (left, middle, right)
postorder = [9,15,7,20,3], (left, right, middle)

Output: 
[3,9,20,null,null,15,7]

"""

from typing import List, Optional


class TreeNode: 
    def __init__(self, val=0, left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    def buildTree(self, inorder:List[int], postorder:List[int])-> Optional[TreeNode]:
        # 1 check if empty 
        if not postorder: 
            return None

        # 2 find the root 
        root_val = postorder[-1]
        root = TreeNode(root_val)

        # 3 find the separator_idx
        separator_idx = inorder.index(root_val)

        # 4 using separator_idx to separate inorder_left/right
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1: ]

        # 5 using inorder_left to find the postorder_left/right
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]

        # 6 recursion 
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        # 7
        return root
