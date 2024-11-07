class Solution:
    def maximumSwap(self, num: int) -> int:
        s=list(str(num))
        maxindex,idx1,idx2=len(s)-1,-1,-1
        for i in range(len(s)-1,-1,-1):
            if s[i]>s[maxindex]:
                maxindex=i
            elif s[i]<s[maxindex]:
                idx1,idx2=i,maxindex
        if idx1==-1:
            return num
        s[idx1],s[idx2]=s[idx2],s[idx1]
        return int("".join(s))