# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=[]
        self.arr=collections.deque()
    def BFS(self,root):
        if not root:
            return
        self.arr.append([root,0])
        while len(self.arr)>0:
            node,level=self.arr.popleft()
            if node:
                if level==len(self.res):
                    self.res.append([])
                self.res[level].append(node.val)
                self.arr.append([node.left,level+1])
                self.arr.append([node.right,level+1])
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.BFS(root)
        return self.res