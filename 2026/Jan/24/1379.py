# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        tofind=target.val
        stack=[]
        stack.append(cloned)
        while stack:
            node=stack.pop()
            if node:
                if node.val==tofind:
                    return node
                stack.append(node.right)
                stack.append(node.left)