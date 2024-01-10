"""
given root1 and root2 
merge two tree


Input: 
root1 = [1,3,2,5], 
root2 = [2,1,3,null,4,null,7]

Output: 
[3,4,5,5,4,null,7]
"""

class TreeNode:
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

class Solution: 
    def mergeTrees(self, root1, root2):
        # ending program
        if not root1:
            return root2 
        if not root2: 
            return root1
        if not root1 and not root2: 
            return None 
        
        # middle 
        newRoot = TreeNode()
        newRoot.val = root1.val + root2.val 

        # left 
        newRoot.left = self.mergeTrees(root1.left, root2.left)
        newRoot.right = self.mergeTrees(root1.right, root2.right)

        return newRoot 