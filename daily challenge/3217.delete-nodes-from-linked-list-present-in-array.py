# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy= ListNode(0,head)
        dummy_cur=dummy

        d=set(nums)

        cur=head
        while cur!=None:
            if cur.val not in d:
                #print(cur.val)
                dummy_cur.next=cur
                dummy_cur=cur
            cur=cur.next
           #print(cur.val)
        dummy_cur.next=None
        return dummy.next