class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        nxt=[0]*n
        prev=[0]*n
        index=k+1
        S=0
        if k==0:
            return [0]*n
        if k>0:
            for i in range(1,k+1):
                S+=code[i]
            nxt[0]=S
            for i in range(1,len(code)):
                nxt[i]=nxt[i-1]-code[i]+code[index%n]
                index+=1
            return nxt
        else:
            k=-k
            index=n-2-k
            for i in range(n-2,n-2-k,-1):
                S+=code[i]
            prev[n-1]=S
            for i in range(n-2,-1,-1):
                prev[i]=prev[i+1]-code[i]+code[index%n]
                index-=1
            return prev
        