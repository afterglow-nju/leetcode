class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        d=defaultdict(int)
        ret=""
        for i in s:
            d[i]+=1
        alpha=list(d.keys())
        alpha.sort(reverse=True)
        left=0
        while left<len(alpha):
            #print(d,left)
            tem=repeatLimit
            if ret and ret[-1]==alpha[left]:
                tem-=1
            ret+=alpha[left]*min(tem,d[alpha[left]])
            d[alpha[left]]-=min(tem,d[alpha[left]])
            if left+1>=len(alpha):
                break
            else: 
                ret+=alpha[left+1]

            d[alpha[left+1]]-=1
            if d[alpha[left+1]]==0:
                del alpha[left+1]

            while left<len(alpha) and d[alpha[left]]==0:
                left+=1
                
        return ret
            

