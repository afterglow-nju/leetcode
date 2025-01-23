# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        cur=head
        d=dict()
        prev=dummy
        while cur:
            if cur.next:
                if cur.next.val==cur.val:
                    v=cur.val
                    while cur and cur.val==v:
                        cur=cur.next
                    prev.next=cur
                else:
                    prev=cur
                    cur=cur.next
            else:
                break

        return dummy.next