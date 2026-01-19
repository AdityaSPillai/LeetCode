# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=None
    def DFS(self,root,p,q):
        if not root:
            return None
        value=root.val
        if value>p.val and value>q.val:
            self.DFS(root.left,p,q)
        elif value<p.val and value<q.val:
            self.DFS(root.right,p,q)
        elif value>=p.val and value<=q.val:
            self.res=root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val>q.val:
            tmp=p
            p=q
            q=tmp
        self.DFS(root,p,q)
        return self.res


#Leetcode Submission
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=None
    def DFS(self,root,p,q):
        if not root:
            return None
        if root.val>p.val and root.val>q.val:
            self.DFS(root.left,p,q)
        elif root.val<p.val and root.val<q.val:
            self.DFS(root.right,p,q)
        elif root.val>=p.val and root.val<=q.val:
            self.res=root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val>q.val:
            tmp=p
            p=q
            q=tmp
        self.DFS(root,p,q)
        return self.res