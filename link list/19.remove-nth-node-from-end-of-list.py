# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index=0
        fast,slow=head,head
        for i in range(n-1):
            fast=fast.next
        prev=None
        while fast.next:
            fast=fast.next
            prev=slow
            slow=slow.next
        
        if prev!=None:
            prev.next=slow.next
            return head
        else:
            return head.next
        









#比较慢
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index=1
        cur=head
        prev=head
        l=0
        while cur:
            cur=cur.next
            l+=1
        n=l-n+1
        cur=head
        while index<n:
            prev=cur
            cur=cur.next
            index+=1
        if prev==cur:
            return cur.next
        prev.next=cur.next
        return head