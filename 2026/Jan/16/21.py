# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=list1,list2
        prev=None
        s=0
        if not curr1:
            return list2
        elif not curr2:
            return list1
        while curr1 or curr2:
            if curr1 and curr2:
                if curr1.val<=curr2.val:
                    if not prev:
                        prev=curr1
                        curr1=curr1.next
                        s=1
                    else:
                        nxt=curr1.next
                        prev.next=curr1
                        prev=curr1
                        curr1=nxt
                elif curr2.val<curr1.val:
                    if prev:
                        nxt=curr2.next
                        curr2.next=prev.next
                        prev.next=curr2
                        prev=curr2
                        curr2=nxt
                    else:
                        nxt=curr2.next
                        prev=curr2
                        curr2=nxt
                        s=2
            elif curr1:
                prev.next=curr1
                prev=curr1
                curr1=curr1.next
            else:
                prev.next=curr2
                prev=curr2
                curr2=curr2.next
            
        return list1 if s==1 else list2