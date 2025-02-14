# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
ListNode.__lt__=lambda a,b:a.val<b.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        for i in lists:
            if i:
                heapq.heappush(h,i)
        dummy=ListNode()
        cur=dummy
        while h:
            node=heapq.heappop(h)
            cur.next=node
            cur=node
            if node.next:
                heapq.heappush(h,node.next)
        return dummy.next
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(list1,list2):
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
            #print(head.next)
            return head.next
        
        m=[]
        while len(lists)>1:
            print(len(lists))
            #assert(0)
            if len(lists)%2==1:
                m.append(lists[-1])
            for i in range(0,len(lists)-1,2):
                tem=merge(lists[i],lists[i+1])
                m.append(tem)
            
            lists=m
            m=[]

        return lists[0] if lists else None
'''
        