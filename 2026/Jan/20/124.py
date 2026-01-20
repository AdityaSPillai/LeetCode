# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=-10**18
    def DFS(self,root):
        if not root:
            return -10**18
        l=self.DFS(root.left)
        r=self.DFS(root.right)
        v=root.val
        vr=v+r
        vl=v+l
        a=v+l+r
        m=max(vr,vl,v)
        print(v,m)
        self.res=max(self.res,m,a)
        return m
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.res