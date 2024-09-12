class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ret=[[-1]*n for i in range(m)]
        cur=head
        index=0
        
        while cur:
            for i in range(index,n-index):
                if not cur:
                    break
                ret[index][i]=cur.val
                cur=cur.next


            for i in range(index+1,m-index):
                if not cur:
                    break
                ret[i][n-1-index]=cur.val
                cur=cur.next


            for i in range(n-1-index-1,index-1,-1):
                if not cur:
                    break
                ret[m-1-index][i]=cur.val
                cur=cur.next


            for i in range(m-1-index-1,index,-1):
                if not cur:
                    break
                ret[i][index]=cur.val
                cur=cur.next
            index+=1
        
        return ret