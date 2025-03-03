# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        cur=dummy
        more=0
        c1,c2=l1,l2
        while c1 or c2:
            v1,v2=0,0
            if c1:
                v1=c1.val
                c1=c1.next
            if c2:
                v2=c2.val
                c2=c2.next
            n=v1+v2+more
            v,more=n%10,n//10
            cur.next=ListNode(v)
            cur=cur.next
            
        if more:
            cur.next=ListNode(more)
            cur=cur.next
        return dummy.next