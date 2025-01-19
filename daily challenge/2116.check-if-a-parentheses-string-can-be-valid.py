class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n=len(s)
        l,r=0,0
        if n&1==1:
            return False
        for i in range(n):
            if s[i]=='(' or locked[i]=='0':
                l+=1
            else:
                if l>0:
                    l-=1
                else:
                    return False
        l=0
        for i in range(n-1,-1,-1):
                if s[i]==')' or locked[i]=='0':
                    l+=1
                else:
                    if l>0:
                        l-=1
                    else:
                        return False
        return True