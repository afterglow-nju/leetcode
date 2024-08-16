class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f,t=0,0
        for i in bills:
            if i==5:
                f+=1
            elif i==10:
                f-=1
                if f<0:
                    return False
                t+=1
            elif i==20:
                f-=1
                if t>0:
                    t-=1
                else:
                    f-=2
                if f<0:
                    return False
        return True