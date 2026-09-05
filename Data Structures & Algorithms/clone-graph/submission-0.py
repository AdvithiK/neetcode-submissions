"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        copymap = {}

        def dfs(node):
            if not node:
                return None
            if node in copymap:
                return copymap[node]
            #create a copy of the current node & store in copymap
            copy = Node(node.val)
            copymap[node] = copy
            #for each neighbor of node, do dfs on it and append to copy's neighbors
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy
        if not node:
            return None
        return dfs(node)




        