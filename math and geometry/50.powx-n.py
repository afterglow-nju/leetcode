class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(a,b):#a^b:
            res=1
            while b>0:
                if b&1:
                    res*=a
                a=a*a
                b>>=1
            return res
        
        
        if n<0:
            return 1/pow(x,-n)
        else:
            return pow(x,n)

