class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #最长公共子序列
        dp=[[0]*(len(text1)+1) for _ in range(1+len(text2))]
        #dp[i][j] stands for the lcs for 0-i-1 and 0-j-1


        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                #dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if text2[i-1]==text1[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]#max(dp[i-1][j-1]+1,dp[i][j])
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                #print(i,j,dp[i][j])
        return dp[len(text2)][len(text1)]
    
    
    
傻逼更快版本，不知道为什么
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #最长公共子序列


        n,m=len(text2),len(text1)
        dp=[[0]*(m+1) for _ in range(1+n)]
        #dp[i][j] stands for the lcs for 0-i-1 and 0-j-1


        for i in range(1,n+1):
            for j in range(1,m+1):
                #dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if text2[i-1]==text1[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]#max(dp[i-1][j-1]+1,dp[i][j])
                else:
                    if dp[i-1][j]>dp[i][j-1]:
                        dp[i][j]=dp[i-1][j]
                    else:
                        dp[i][j]=dp[i][j-1]
                    #dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                #print(i,j,dp[i][j])
        return dp[n][m]