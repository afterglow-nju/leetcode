class Solution:
    def getLucky(self, s: str, k: int) -> int:
        integer=0
        for i in s:
            #if ord(i)-ord('a')+1>=10:
            integer=integer*100+ord(i)-ord('a')+1
           # else:
            #    integer=integer*10+ord(i)-ord('a')+1
            #print(ord(i)-ord('a')+1,integer)
        tem=integer
        ret=integer
        #print(integer)
        for i in range(k):
            tem=ret
            ret=0
            while tem:
                ret=ret+tem%10
                tem//=10
        return ret
                