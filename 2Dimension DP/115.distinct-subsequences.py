class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1,l2=len(s),len(t)
        if l1<l2:
            return 0
        
        dp=[[0]*(l2+1) for _ in range(l1+1)]

        for i in range(l1):
            dp[i][0]=1
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if i<j:
                    continue

                dp[i][j]=dp[i-1][j]
                if s[i-1]==t[j-1]:
                    dp[i][j]+=dp[i-1][j-1]
           
        return dp[l1][l2]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1,n2=len(s),len(t)
        if n1<n2:
            return 0
        
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0]=1
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                dp[i][j]=dp[i-1][j]
                if s[i-1]==t[j-1]:
                    dp[i][j]+=dp[i-1][j-1]

        return dp[n1][n2]