# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head,k):

            cur=head
            prev=None
            while k:
                n=cur.next
                cur.next=prev
                prev=cur
                cur=n
                k-=1

            #1,2,3  =  3,2,1
            #head=3, tail=1
            Head,Tail=prev,head
            return Head,Tail
        
        cur=head
        i=1
        old_tail=None
        old_head=None
        beg=head
        while cur:
            #print(i,cur.val)
            if i%k==0:
                tem=cur.next
                Head,Tail=reverse(beg,k)
                beg=tem
                #print(Head,k,i)

                if not old_tail:
                    old_tail=Tail
                    old_head=Head
                else:
                    old_tail.next=Head
                    old_tail=Tail
                cur=tem
        
            else:
                cur=cur.next
            i+=1
        old_tail.next=beg
        return old_head
            



