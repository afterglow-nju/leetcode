class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        res=0
        for i in range(2,n+1):
            res=(res+k)%i
        return (res+1)%(n+1)

        '''
        l1,d=list(range(0,n)),defaultdict(int)
        ret=n
        index,c=0,0
        while ret>1:
            
            #print(index,d[index],ret)
            if d[index]==0:
                c+=1
                if c==k:
                    d[index]=1
                    ret-=1
                    c=0
        #    print(d,c)
            index+=1
            index%=n
        #print(index,d[index])
        while d[index]==1:
            index+=1
            index%=n
        return (index+1)%(n+1)
        '''