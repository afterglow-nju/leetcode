#这样更快
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret=0
        while n>0:
            ret+=(n&1)
            n>>=1
        return ret

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret=0
        while n>0:
            ret+=(n%2)
            n>>=1
        return ret