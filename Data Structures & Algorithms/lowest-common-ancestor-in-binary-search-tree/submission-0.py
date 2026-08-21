# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #start from the root and go down until p & q split
        node = root

        while node:
            if  node.val < p.val and node.val < q.val:
                #explore the right sub tree to get a greater root val
                node = node.right
            elif node.val > p.val and node.val > q.val:
                #explore the left sub tree to get a lesser root val
                node = node.left
            else:
                #greatest root found
                return node

        