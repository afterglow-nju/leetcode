class Solution:
    def findComplement(self, num: int) -> int:
        s =bin(num)
        ret=''
        for i in s[2:]:
            if i=='0':
                ret+='1'
            else:
                ret+='0'
        #print(s[2:],ret)
        return int(ret,2)