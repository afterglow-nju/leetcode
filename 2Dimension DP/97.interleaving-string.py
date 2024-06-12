class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1,n2,n3=len(s1),len(s2),len(s3)
        if n1+n2!=n3:
            return False
        dp=[[False]*(n1+1) for _ in range(n2+1)]
        
        dp[0][0]=True
        for i in range(0,n2+1): #s2
            for j in range(0,n1+1):#s1
                if j>0 and i>0:
                    dp[i][j]=(dp[i][j-1] and s1[j-1]==s3[i+j-1]) or \
                         (dp[i-1][j] and s2[i-1]==s3[i+j-1])
                elif j>0:
                    dp[i][j]=(dp[i][j-1] and s1[j-1]==s3[i+j-1])
                elif i>0:
                    dp[i][j]=(dp[i-1][j] and s2[i-1]==s3[i+j-1])
                #print(i,j,dp[i][j])
        return dp[n2][n1]
                





class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s2)<len(s1):
            s1,s2=s2,s1
        if len(s2)+len(s1)!=len(s3):
            return False
        
        dp=[[False]*(len(s1)+1) for _ in range(1+len(s2))]


        dp[0][0]=True
        
        for i in range(0,len(s2)+1):
            for j in range(0,len(s1)+1):
                if j>0:
                    dp[i][j]=s1[j-1]==s3[i+j-1] and dp[i][j-1]
                if i>0:
                    dp[i][j]|=s2[i-1]==s3[i+j-1] and dp[i-1][j]
                
        return dp[len(s2)][len(s1)]