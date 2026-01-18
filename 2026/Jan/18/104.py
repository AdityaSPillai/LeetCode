# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

# Iterative DFS
class Solution:
    def __init__(self):
        self.stack=[]
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.stack.append((root,1))
        maxD=1
        while len(self.stack)>0:
            node,depth=self.stack.pop()
            maxD=max(maxD,depth)
            if node:
                r,l=node.right,node.left
                if r:
                    self.stack.append((r,depth+1))
                if l:
                    self.stack.append((l,depth+1))
        return maxD

#BFS
class Solution:
    def __init__(self):
        self.queue=collections.deque()
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.queue.append([root,1])
        maxL=1
        while len(self.queue)>0:
            node,level=self.queue.popleft()
            maxL=max(maxL,level)
            if node:
                l,r=node.left,node.right
                if l:
                    self.queue.append([l,level+1])
                if r:
                    self.queue.append([r,level+1])
        return maxL