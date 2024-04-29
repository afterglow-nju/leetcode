# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur=l1
        head=None
        ret=None
        t=0
        while l1 or l2:
            if l1 and l2:
                val=l1.val+l2.val
                l1=l1.next
                l2=l2.next
                val=val+t
                t=val//10
                tem=ListNode(val=val%10)
                if not head: #如果要改进，这里直接dummy head，然后用next
                    head=tem
                    ret=head
                else:
                    head.next=tem
                    head=head.next
            elif l1:
                val=l1.val+t
                t=val//10
                tem=ListNode(val=val%10)
                head.next=tem
                head=head.next
                l1=l1.next
            elif l2:
                val=l2.val+t
                t=val//10
                tem=ListNode(val=val%10)
                head.next=tem
                head=head.next
                l2=l2.next
        if t:
            tem=ListNode(val=1)
            head.next=tem
        return ret
        
        