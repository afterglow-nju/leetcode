class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        f=[0]*(n+1)
        valid=set()
        for i in range(1,27):
            valid.add(str(i))
        
        if s[0] not in valid:
            return 0
        else:
            f[0]=1

        if len(s)>1 and s[1] in valid:
            f[1]=1
        
        if s[0:2] in valid:
            f[1]+=1
        
        
        for i in range(2,n):

            b1=s[i] in valid 
            b2=s[i-1:i+1] in valid
            #print(f[i-2],f[i-1])
            if b1 and b2:
                #print("aa")
                f[i]=f[i-1]+f[i-2] #画图想清楚了，为什么是加
            elif b1:
                #print("!")
                f[i]=f[i-1]
            elif b2:
                #print(s[i-1:i+1],">")
                f[i]=f[i-2]
            else:
                return 0

        return f[n-1]