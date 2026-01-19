# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=0
    def DFS(self,root,tmax):
        if not root:
            return None
        if tmax<=root.val:
            print(root.val)
            print("tmax",tmax)
            self.res+=1
            tmax=max(tmax,root.val)
        self.DFS(root.left,tmax)
        self.DFS(root.right,tmax)
    def goodNodes(self, root: TreeNode) -> int:
        self.DFS(root,root.val)
        return self.res