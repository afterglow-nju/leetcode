class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        x=0xffffffff
        #print(a,b,a&x,b&x)
        a, b = a & x, b & x
        while b!=0:
            t=(a&b)<<1
            a=a^b
            b=t&x
            #print(b)
        return  a if a <= 0x7fffffff else ~(a ^ x)


        while And!=0:
            And<<=1
            newxor=And^Xor
            newAnd=And&Xor
            #print(newxor,newAnd)
            And=newAnd
            Xor=newxor
        return Xor