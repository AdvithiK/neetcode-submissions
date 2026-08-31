# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #use dfs to build the tree using preorder for roots & inorder for building the tree
        preIdx, inIdx = 0,0

        #recursive function dfs to build the tree unit a limit val to stop building the left subtree
        def dfs(limit):
            nonlocal preIdx,inIdx
            if preIdx >= len(preorder):
                return None
            #if limit is hit, left subtree is built complete
            if inorder[inIdx] == limit:
                inIdx += 1
                return None
            
            root = TreeNode(preorder[preIdx])
            preIdx +=1

            #build the left subtree with everything left of root
            root.left = dfs(root.val)

            #build right subtree using the limit
            root.right = dfs(limit)
            return root

        #return dfs using inf (large val)
        return dfs(float('inf'))



            
        

        