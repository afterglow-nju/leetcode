class Solution:
    def reverseBits(self, n: int) -> int:
        
        ret=0
        for i in range(32):
            ret=(ret<<1)|(n&1)
            n>>=1
            #ret<<=1
        return ret

class Solution:
    def reverseBits(self, n: int) -> int:
        
        s=format(n, '032b')
        power=[1]*32
        for i in range(1,32):
            power[i]=power[i-1]<<1
        ret=0
        for i in range(len(s)):
            if s[i]=='1':
                ret+=power[i]
        return ret
        