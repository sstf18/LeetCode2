"""
lowest common ancestor: between two nodes p and q as the lowest node in T that has both pand q as descendants

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
"""

class TreeNode: 
    def __init__(self, val=0, left = None, right = None): 
        self.val = val 
        self.left = left 
        self.right = right 

class Solution: 
    # step 1 
    def lowestCommonAncestor(self, root:'TreeNode', p:'TreeNode', q:'TreeNode') -> 'TreeNode':
        
        # step 2 
        if not root: 
            return None 
        if root == p or root == q: 
            return root 
        # step 3

        # left 
        left = self.lowestCommonAncestor(root.left, p, q)
        # right 
        right = self.lowestCommonAncestor(root.right, p, q)
        # middle 
        if left and right: # left/right both exist, directly return root
            return root 
        if left and not right: # left exsit, return left
            return left 
        elif not left and right: # right exsit, return right
            return right 
        else: 
            return None 