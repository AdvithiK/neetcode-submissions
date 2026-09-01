# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #using dfs
        #set root to final res
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            #set the left and right to max between it and 0
            left = max(left, 0)
            right = max(right, 0)

            #set res to the max between curr res & new traversal
            res[0] = max(res[0], node.val + left + right)
            #return the res + either left or right subtree
            return node.val + max(left, right)
        dfs(root)
        return res[0]
