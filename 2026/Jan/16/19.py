# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        leng=0
        while curr:
            curr=curr.next
            leng+=1
        curr=head
        first=True
        if leng==1:
            return None
        for _ in range(leng-n):
            first=False
            prev=curr
            curr=curr.next
        if first:
            return curr.next
        else:
            prev.next=curr.next
            return head