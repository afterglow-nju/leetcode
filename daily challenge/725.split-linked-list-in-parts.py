# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ret=[]
        l=0
        cur=head
        while cur:
           l+=1
           cur=cur.next
        cur=head
        if l<=k:
            while cur:
                tem=cur
                cur=cur.next
                tem.next=None
                ret.append(tem)
            for i in range(k-l):
                ret.append(None)
        else:       
            addition=l%k
            for i in range(addition):
                tem=cur
                ret.append(tem)
                for i in range(l//k):
                    tem=tem.next
                    cur=cur.next
                cur=cur.next
                tem.next=None
                
            while cur:
                tem=cur
                ret.append(tem)
                for i in range(l//k-1):
                    tem=tem.next
                    cur=cur.next
                cur=cur.next
                tem.next=None
                
        return ret
            