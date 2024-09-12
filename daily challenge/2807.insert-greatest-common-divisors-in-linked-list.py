# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        while cur.next:
            a,b=cur.val,cur.next.val
            tem=math.gcd(a,b)
            #print(a,b,math.gcd(a,b),tem)
            newnode=ListNode(tem,cur.next)
            cur_tem=cur.next
            cur.next=newnode
            cur=cur_tem
        return head