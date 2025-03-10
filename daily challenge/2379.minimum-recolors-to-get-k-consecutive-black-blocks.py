class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        pre=[0]*(1+n)
        for i in range(n):
            pre[i+1]=pre[i]
            if blocks[i]=='B':
                pre[i+1]+=1
        ret=k
        #print(pre)
        for i in range(0,n-k+1):
            #print(i,pre[i],pre[i+k])
            ret=min(ret,k-(pre[i+k]-pre[i]))
        return ret
