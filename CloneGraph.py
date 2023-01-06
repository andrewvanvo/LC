
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hm = {}
        if not node:
            return node
        def dfs(node):
            if node in hm:
                return hm[node]
            copy = Node(node.val)
            hm[node] = copy
            for nb in node.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy

        return dfs(node)