class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k==1:
            return '0'
        if k==2**(n-1):
            return '1'
        else:
            if k<2**(n-1):
                return self.findKthBit(n-1,k)
            else:
                return '0' if self.findKthBit(n-1,2**n-k)=='1' else '1'







class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        t='0'
        for i in range(1,n):
            tem=''
            for j in t:
                if j=='1':
                    tem+='0'
                else:
                    tem+='1'
            t=t+'1'+tem[::-1]
        return t[k-1]