# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #recursive soln

        #check if we reach the end/null
        if not root:
            return None
        #constantly switch the left and right child
        temp = root.left
        root.left = root.right
        root.right = temp

        #recursively flip the left tree
        self.invertTree(root.left)
        #recursively flip the right tree
        self.invertTree(root.right)

        return root
        
        