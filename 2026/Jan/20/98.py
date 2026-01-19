# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=True
    def DFS(self,root):
        if not root:
            return None,None
        lmin,lmax=self.DFS(root.left)
        rmin,rmax=self.DFS(root.right)
        lmin=10**18 if lmin==None else lmin
        rmin=10**18 if rmin==None else rmin
        lmax=-10**18 if lmax==None else lmax
        rmax=-10**18 if rmax==None else rmax
        if lmax>=root.val and lmax!=-10**18:
            self.res=False
        elif lmin>=root.val and lmin!=10**18:
            self.res=False
        elif rmax<=root.val and rmax!=-10**18:
            self.res=False
        elif rmin<=root.val and rmin!=10**18:
            self.res=False
        return min(root.val,lmin,rmin),max(root.val,lmax,rmax)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.DFS(root)
        return self.res