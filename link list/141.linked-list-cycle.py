# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head.next if head else None
        while fast and fast.next:
            if slow.val==fast.val and slow.next==fast.next:
                return True
            else:
                fast=fast.next.next
                slow=slow.next
        return False
    
下面是偷鸡方法 :joy:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur=head
        while cur:
            if cur.val=='1':
                return True
            else:
                cur.val='1'
                cur=cur.next
        return False