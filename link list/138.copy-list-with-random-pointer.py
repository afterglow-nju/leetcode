"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#共有n个，random是随机指向一个node
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        #Head=Node(head.val)
        #curr=Head
        dic=dict()
        '''
        while cur:
            tem=Node(cur.val)
            curr.next=tem
            curr=curr.next
            cur=cur.next
        curr.next=None
        '''
        while cur:
            dic[cur]=Node(cur.val)
            cur=cur.next
        
        cur=head
        while cur:
            dic[cur].next=dic.get(cur.next,None)
            dic[cur].random=dic.get(cur.random,None)
            cur=cur.next

        return dic.get(head)
        