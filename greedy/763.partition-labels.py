class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d=defaultdict(lambda:-1)
        for i in range(len(s)):
            d[s[i]]=i
        S=set()
        ret=[]
        pre,mmax=0,d[s[0]]
        S.add(s[0])
        for i in range(1,len(s)):
            if i>mmax:
                ret.append(i-pre)
                pre=i
                S.clear()
                S.add(s[i])
                mmax=d[s[i]]
            else:
                if s[i] not in S:
                    S.add(s[i])
                    mmax=max(mmax,d[s[i]])
        if S:
            ret.append(len(s)-pre)
        return ret
