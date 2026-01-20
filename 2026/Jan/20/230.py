# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth=0
        arr=[]
        curr=root
        while curr or arr:
            while curr:
                arr.append(curr)
                curr=curr.left
            curr=arr.pop()
            kth+=1
            if kth==k:
                return curr.val
            curr=curr.right