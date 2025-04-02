class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        ret=[]
        left=0
        S=set()
        for right in range(len(s)):
            S.add(s[right])
            d[s[right]]-=1
            #print(S)
            if d[s[right]]==0:
                S.remove(s[right])
                if len(S)==0:
                    ret.append(right-left+1)
                    left=right+1
        return ret