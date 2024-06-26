class Solution:
    def checkValidString(self, s: str) -> bool:
        l,r,b,c=0,0,0,0
        for i in s:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            else:
                r+=1 #先把*都当做）
                c+=1 #c代表有多少*

            if l>=r:
                continue
            else:
                #print(r,l,c,b)
                if r-l<=c: #r太大，但是还在c的范围内
                    c-=(r-l) # *少了这么多，当成空串了，所以r减少到l这么多
                    b+=(r-l) # b代表可用作（的*的数量
                    r=l
                elif r-l<=b: # 发现把*当空串，不当成）还是不够，所以把b的*当做（
                    b-=(r-l) #所以是l变多，变到r这么多
                    l=r
                else:
                    return False
        
        return l==r
             