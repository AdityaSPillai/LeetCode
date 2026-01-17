# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        originalcurr1=lists[0]
        for i in range(len(lists)-1):
            prev=None
            curr1,curr2=originalcurr1,lists[i+1]
            print()
            while curr1 and curr2:
                if curr1.val<=curr2.val:
                    if prev:
                        prev.next=curr1
                    prev=curr1
                    curr1=curr1.next
                else:
                    if prev:
                        prev.next=curr2
                    else:
                        originalcurr1=curr2
                    prev=curr2
                    curr2=curr2.next
            while curr1:
                if prev:
                    prev.next=curr1
                prev=curr1
                curr1=curr1.next
            while curr2:
                if prev:
                    prev.next=curr2
                else:
                    originalcurr1=curr2
                prev=curr2
                curr2=curr2.next
        return originalcurr1