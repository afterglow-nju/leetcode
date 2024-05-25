class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        f=[[True]*n for i in range(n)]
        
        ret=0
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                f[i][j]=f[i+1][j-1] and s[i]==s[j]
                #print(f[i][j])
                if f[i][j]:
                    ret+=1
        
        return ret+n







class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        f=[[1]*n for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                f[i][j]=0
        ret=0
        for index in range(1,n):
            for j in range(n-1,index-1,-1):
                i=j-index
                #print(i,j,i+1,j-1)
                if f[i+1][j-1]==1 and s[i]==s[j]:
                    f[i][j]=1
                    #print(i,j)
                    ret+=1
                else:
                    f[i][j]=0
        
        return ret+n