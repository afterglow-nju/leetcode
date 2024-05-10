class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f=[1]*(n+1)
        for i in range(1,len(f)):
            f[i]=i*f[i-1]
        ans=0
        valid=[1]*(n+1)
        k=k-1
        for i in range(n,0,-1):
            t=k//f[i-1]+1 #余数从0开始
            #print("i=",i,"t=",t)
            for j in range(1,n+1):
                t-=valid[j]
                if t==0:
                    ans=ans*10+j
                    valid[j]=0
                    break
            #print(ans)
            k=k%f[i-1]
        return str(ans)