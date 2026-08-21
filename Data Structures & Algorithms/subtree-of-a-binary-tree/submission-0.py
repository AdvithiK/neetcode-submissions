# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #recursive dfs
        if not subRoot:
            return True
        if not root:
            return False

        #check the helper function truth
        if self.helperTree(root, subRoot):
            return True
    
        #continue checking the tree dfs
        return (self.isSubtree(root.left, subRoot) or                      self.isSubtree(root.right, subRoot))

    #recursive helper function checking similarity
    def helperTree(self, root:Optional[TreeNode], subRoot:Optional[TreeNode]) -> bool:
        
        #recurive edge case to return all
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
                #recursively call to check truth in left and right of node
                return (self.helperTree(root.left, subRoot.left) and self.helperTree(root.right, subRoot.right))
        
        return False


        
