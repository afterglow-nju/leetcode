class Solution:
    def reorganizeString(self, s: str) -> str:
        C = [[char, freq] for char, freq in Counter(s).most_common()]
        if C[0][1]>len(s)-C[0][1]+1:
            return ""
        ans=[""]*len(s)
        index=0
        n=len(s)
        for i in range(0,n,2):
            ans[i]=C[index][0]
            C[index][1]-=1
            if C[index][1]==0:
                index+=1
        for i in range(1,n,2):
            ans[i]=C[index][0]
            C[index][1]-=1
            if C[index][1]==0:
                index+=1
        return "".join(ans)