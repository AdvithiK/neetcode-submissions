# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #use a queue, bfs
        tree_queue = deque()
        tree_queue.append(root)
        #store the result of sublist levels
        res = []

        #while the queue is not empty
        while len(tree_queue) != 0:
            children = []
            #track the len of queue for the for loop
            qlen = len(tree_queue)
            
            #for loop to grab each level at a time
            for i in range(qlen):
                explore_node = tree_queue.popleft()

                if explore_node:
                    children.append(explore_node.val)
                    tree_queue.append(explore_node.left)
                    tree_queue.append(explore_node.right)
            #check that sublist is not empty
            if children:
                #append the sublist to result
                res.append(children)
        return res





        