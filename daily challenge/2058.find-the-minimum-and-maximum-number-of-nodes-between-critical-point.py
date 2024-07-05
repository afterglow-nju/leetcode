# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur=head.next
        pre=head
        ret=[]
        index=1
        while cur.next:
#            if cur.next:
            if pre.val<cur.val and cur.val>cur.next.val:
                ret.append(index)
                #print("?",index)
            elif pre.val>cur.val and cur.val<cur.next.val:
                ret.append(index)
                #print("!",index)
            index+=1
            pre=cur
            cur=cur.next
        t=float('inf')
        if len(ret)>=2:
            for i in range(1,len(ret)):
                t=min(t,ret[i]-ret[i-1])
            return [t,ret[-1]-ret[0]]
        else:
            return [-1,-1]