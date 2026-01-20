# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.arr=collections.deque()
        self.first=1
        self.res=None
        self.prevend=None
        self.j=0
    def traverse(self,head,k):
        if not head:
            return None
        self.arr.append(head)
        nxt=head.next
        i=0
        if len(self.arr)==k:
            while len(self.arr)>0:
                node=self.arr.popleft()
                if self.first==1:
                    self.res=node
                    self.first=-1
                if i==0 and head.next:
                    node.next=head.next
                    prev=node
                    previous=self.prevend
                    self.prevend=node
                    i=1
                elif i==0:
                    node.next=None
                    previous=self.prevend
                    prev=node
                    i=1
                else:
                    node.next=prev
                    prev=node
                self.first-=1
            if self.j!=0:
                previous.next=prev
            self.j=1
        if nxt:
            self.traverse(nxt,k)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.res=head
        self.first=k
        self.traverse(head,k)
        return self.res