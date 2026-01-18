# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def DFS(self,root):
        if not root:
            return 0
        l,r=self.DFS(root.left),self.DFS(root.right)
        if l-r not in [-1,0,1]:
            self.res=1
        return 1+max(l,r)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.DFS(root)
        return True if self.res==0 else False