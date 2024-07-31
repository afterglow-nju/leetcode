class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1[0]=='0' or num2[0]=='0':
            return "0"
        
        num1,num2=num1[::-1],num2[::-1]
        ret=[0]*(len(num1)+len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit=int(num1[i])*int(num2[j])
                ret[i+j]+=digit
                ret[i+j+1]+=ret[i+j]//10
                ret[i+j]%=10
        ret=ret[::-1]
        beg=0
        while beg<len(num1)+len(num2) and ret[beg]==0:
            beg+=1
        ret=list(map(str,ret))
        s="".join(ret[beg:])
        return s
        #return str(eval(num1)*eval(num2))