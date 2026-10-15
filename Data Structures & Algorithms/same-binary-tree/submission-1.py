# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if we reach null nodes
        if not p and not q:
            return True
        
        #check if one node doesn't exist or if root vals match
        if not p or not q or p.val != q.val:
            return False
        
        #recursively traverse the tree left == right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        