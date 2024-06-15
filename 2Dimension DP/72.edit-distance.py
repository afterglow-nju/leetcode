class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2=len(word1),len(word2)
        if l1<l2:
            word1,word2=word2,word1
            l1,l2=l2,l1
        #l1长
        dp=[[l1]*(l2+1) for _ in range(l1+1)] #(l1+1)*(l2+1)
        dp[0][0]=0
        for i in range(l1+1):
            dp[i][0]=i
        for i in range(l2+1):
            dp[0][i]=i

        # pointer i to word1
        # dp[i][j] stands for distance for word1[0:i] becoming word2[0:j] 
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    # replace delete insert 

        return dp[l1][l2]
        