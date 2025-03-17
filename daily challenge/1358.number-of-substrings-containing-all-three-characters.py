class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d=defaultdict(int)
        ret=0
        n=len(s)
        right=0
        i=0  
        while right<n:
            d[s[right]]+=1
            while i<n-3+1 and len(d.keys())==3:
                #print(i,right,d)
                ret+=(n-1-min(n-1,right)+1)
                d[s[i]]-=1
                if d[s[i]]<=0:
                    del d[s[i]]
                i+=1
            right+=1
        return ret