# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # slow in mid, fast in end
        prev=None
        t=slow.next
        slow.next=None
        slow=t
        while slow:
            
            t=slow.next
            slow.next=prev
            prev=slow
            slow=t
            
        cur1,cur2=head,prev

        while cur2:

            t1=cur1.next
            t2=cur2.next

            cur1.next=cur2
            cur2.next=t1
            cur1=t1
            cur2=t2
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#额外空间
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l=list()
        cur=head
        while cur:
            l.append(cur)
            cur=cur.next
        n=len(l)
        cur=head
        
        for i in range(n//2):
            cur=l[i]
            t=cur.next
            cur.next=l[n-i-1]
            cur.next.next=t
            
        l[n//2].next=None
        return head 
        
        