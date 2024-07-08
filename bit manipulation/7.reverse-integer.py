class Solution:
    def reverse(self, x: int) -> int:
        f=1 if x>0 else -1
        x=abs(x)
        ret=0
        while x>0:
            ret=ret*10+(x%10)
            x//=10
        return f*ret if -2**31<=f*ret<=2**31-1 else 0