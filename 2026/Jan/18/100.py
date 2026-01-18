# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res=0
    def DFS(self,root1,root2):
        if not root1 and not root2:
            return
        elif not root1:
            self.res=1
            return
        elif not root2:
            self.res=1
            return
        if root1.val!=root2.val:
            print("Value not match")
            self.res=1
            return
        self.DFS(root1.left,root2.left)
        self.DFS(root1.right,root2.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.DFS(p,q)
        return True if self.res==0 else False