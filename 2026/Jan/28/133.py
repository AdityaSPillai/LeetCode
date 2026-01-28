"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        nhm={}
        def createNew(node):
            newNode=Node(node.val)
            nhm[node]=newNode
            for i in node.neighbors:
                if i not in nhm:
                    created=createNew(i)
                    newNode.neighbors.append(created)
                else:
                    newNode.neighbors.append(nhm[i])
            return newNode
        return createNew(node)