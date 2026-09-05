"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        #return if none
        if not node:
            return None

        #create a copy map to store nodes
        copymap = {}

        def dfs(node):
            #return the node if in copymap
            if node in copymap:
                return copymap[node]
            #create a copy of the current node & store in copymap
            copy = Node(node.val)
            copymap[node] = copy
            #for each neighbor of node, do dfs on it and append to copy's neighbors
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        return dfs(node)




        