class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def sn(s:str):
            return ord(s)-ord('a')
        
        l1,l2=len(s1),len(s2)
        if l1>l2:
            return False
        d1=[0]*26
        d2=[0]*26
        for i in s1:
            d1[ord(i)-ord('a')]+=1

        for i in range(l1):
            d2[sn(s2[i])]+=1
        if d1==d2:
            return True
        for i in range(1,l2-l1+1):
            #print(d1,d2)
            d2[sn(s2[i-1])]-=1
            d2[sn(s2[i+l1-1])]+=1
            if d1==d2:
                return True
            
        return False