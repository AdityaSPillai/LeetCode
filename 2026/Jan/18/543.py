# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#DFS
class Solution:
    def __init__(self):
        self.res=0
    def DFS(self,root):
        if not root:
            return 0
        l,r=self.DFS(root.left),self.DFS(root.right)
        self.res=max(self.res,l+r)
        return 1+max(l,r) 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.res