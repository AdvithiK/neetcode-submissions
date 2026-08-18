# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #dfs
        #return 0 if leaf or no root
        if not root:
            return 0
        #+1 one coming back up the tree, between the max depth of L or R
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        