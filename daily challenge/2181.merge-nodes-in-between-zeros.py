# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret=ListNode()
        cur=ret
        c=head
        while c:
            t=0
            if c.val==0:
                c=c.next
                while c and True:
                    if c.val!=0:
                        t+=c.val
                        c=c.next
                    else:
                        #c=c.next
                        cur.next=ListNode(t)
                        cur=cur.next
                        break
        return ret.next