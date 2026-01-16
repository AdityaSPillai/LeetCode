#NeetCode Submission

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2=l1,l2
        prev=None
        carry=0
        while curr1 and curr2:
            val1=curr1.val
            val2=curr2.val
            add=val1+val2+carry
            if add>=10:
                carry=1
                add=add%10
            else:
                carry=0
            curr1.val=add
            if prev:
                prev.next=curr1
            prev=curr1
            curr1=curr1.next
            curr2=curr2.next
        while curr1:
            val1=curr1.val
            add=val1+carry
            if add>=10:
                carry=1
                add=add%10
            else:
                carry=0
            newNode=ListNode(add)
            prev.next=newNode
            prev=newNode
            curr1=curr1.next
        while curr2:
            val2=curr2.val
            add=val2+carry
            if add>=10:
                carry=1
                add=add%10
            else:
                carry=0
            newNode=ListNode(add)
            prev.next=newNode
            prev=newNode
            curr2=curr2.next
        if carry==1:
            newNode=ListNode(carry)
            prev.next=newNode
        return l1