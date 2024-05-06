# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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

#这是logk*n


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def compare(bank):
            min=float('inf')
            if not bank:
                return None
            ret=bank[0]
            for i,n in enumerate(bank):
                if n is None:
                    continue
                elif min>n.val:
                    min=n.val
                    ret=n
                    bank.insert(0,bank.pop(i))
            #print("herer",bank,ret)
            bank[:] = [i for i in bank if i]
            if len(bank)!=0:
                bank[0]=bank[0].next if len(bank)!=0 and bank[0] else None
            return ret

        bank=[]
        for i in lists:
            bank.append(i)
        head=compare(bank)
        cur=head
        while True:
            tem=compare(bank)
            if tem:
                if not cur:
                    cur=tem
                else:
                    cur.next=tem
                cur=cur.next
            else:
                break
        return head
        
        
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        
        
        try:
            Cur=lists[0]
            for i in range(len(lists)-1):
                Cur=merge(Cur,lists[i+1])
        except:
            Cur=None
        return Cur