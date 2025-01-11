class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        d=Counter(s)
        c=0
        for value in d.values():
            if value&1==1:
                c+=1
                
        return c<=k and len(s)>=k