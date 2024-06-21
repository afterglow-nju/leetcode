class Solution:
    def checkValidString(self, s: str) -> bool:
        l,r,b,c=0,0,0,0
        for i in s:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            else:
                #b+=1
                r+=1
                c+=1

            if l>=r:
                continue
            else:
                if r-l<=c:
                    c-=(r-l)
                    r=l
                    b+=1
                elif r-l<=b:
                    b-=(r-l)
                    l=r
                else:
                    return False
        
        return l==r
             