class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l1,l2=len(s),len(p)
        dp=[[False]*(l2+1) for _ in range(l1+1)]
        dp[0][0]=True
        for j in range(2, l2+1, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'


        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if p[j-1]=='*':
                    dp[i][j]=dp[i][j-2] or \
                             (dp[i-1][j] and s[i-1]==p[j-2]) or \
                             (dp[i-1][j] and p[j-2]=='.')
                else:
                    dp[i][j]=(dp[i-1][j-1] and s[i-1]==p[j-1]) or \
                                (dp[i-1][j-1] and p[j-1]=='.')
                '''
                if p[j-1]!='.' and p[j-1]!='*':
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
                elif p[j-1]=='.':
                    dp[i][j]=dp[i][j-1]
                elif p[j-1]=='*':
                    # *=0
                    dp[i][j]=dp[i][j-2] or \
                            (s[i-1]==p[j-2] and dp[i-1][j-1]) or \
                            (p[j-2]=='.')# and dp[i-1][j])
                print(i,j,dp[i][j])
                '''
        return dp[l1][l2]