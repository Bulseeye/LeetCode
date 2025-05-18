"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newGraph = {}

        def clone(node):
            if node in newGraph:
                return newGraph[node]
            
            # copy the node to a new node.
            copy = Node(node.val)
            newGraph[node] = copy

            # for every neighbor in the original graph append to the new one
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            # after loop return the new one
            return copy
        # run clone function if we have atleast 1 node
        return clone(node) if node else None
