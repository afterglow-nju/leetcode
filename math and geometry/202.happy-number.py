class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        s.add(n)
        while True:
            ret=0
            while n:
                ret+=(n%10)**2
                n//=10
            n=ret
            if ret==1:
                return True
            if ret not in s:
                s.add(ret)
            else:
                return False
            #print(n)