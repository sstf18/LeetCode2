"""
LCA in BST, using the def of BST

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: 
    def lowestCommonAncestor(self, root: 'TreeNode', p:'TreeNode', q:'TreeNode') -> 'TreeNode':
        if not root: 
            return None 
        # left 
        if p.val < root.val and q.val < root.val: 
            left = self.lowestCommonAncestor(root.left, p, q)
            if left: 
                return left

        # right 
        if p.val > root.val and q.val > root.val: 
            right = self.lowestCommonAncestor(root.right, p, q)
            if right: 
                return right 

        #####################################################
        """
        # second method: simple version of recursion
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else: 
            return root 
        """


        ########################################################
        """
        # third method: iterator 
        while root: 
            if p.val < root.val and q.val < root.val: 
                root = root.left 
            elif p.val > root.val and q.val > root.val: 
                root = root.right
            else: 
                return root 
        return None
        
        """
        
