# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=ListNode(-1)
        cur=head
        head.next=None
        while list1!=None and list2!=None:
            #print(list1,list2)
            if list1  and list2:
                if list1.val<=list2.val:
                    cur.next=list1
                    list1=list1.next
                    cur=cur.next
                else:
                    cur.next=list2
                    list2=list2.next
                    cur=cur.next
        if list1:
            cur.next=list1
        else:
            cur.next=list2
        return head.next
    
    
    
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        try:
            if list1.val<=list2.val:
                head=list1
                list1=list1.next
            else:
                head=list2
                list2=list2.next
        except:
            if list1:
                return list1
            else:
                return list2
        cur=head
        head.next=None
        while list1!=None or list2!=None:
            #print(list1,list2)
            if list1  and list2:
                print(list1,list2)
                if list1.val<=list2.val:
                    cur.next=list1
                    list1=list1.next
                    print(list1)
                    cur=cur.next
                    cur.next=None
                else:
                    cur.next=list2
                    list2=list2.next
                    cur.next.next=None
                    cur=cur.next
            elif list1!=None:
                cur.next=list1
                list1=list1.next
                cur.next.next=None
                cur=cur.next
            elif list2!=None:
                cur.next=list2
                list2=list2.next
                cur.next.next=None
                cur=cur.next
            else:
                print(list1,list2)
                assert(0)
        return head