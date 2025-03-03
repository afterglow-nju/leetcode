class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s=list(int(i) for i in s)
        while len(s)>2:
            tem=[]
            for i in range(len(s)-1):
                tem.append((s[i]+s[i+1])%10)
            s=tem
            
        return s[0]==s[1]
        