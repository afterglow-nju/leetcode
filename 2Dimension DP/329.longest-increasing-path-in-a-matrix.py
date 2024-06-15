class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[False]*n for _ in range(m)]
        ret=0

        def dfs(i,j):
            if dp[i][j]!=False:
                return dp[i][j]
            else:
                if i-1>=0 and matrix[i][j]<matrix[i-1][j]:
                    dp[i][j]=max(dp[i][j],dfs(i-1,j)+1)

                if j-1>=0 and matrix[i][j]<matrix[i][j-1]:
                    dp[i][j]=max(dp[i][j],dfs(i,j-1)+1)

                if i+1<m and matrix[i][j]<matrix[i+1][j]:
                    dp[i][j]=max(dp[i][j],dfs(i+1,j)+1)

                if j+1<n and matrix[i][j]<matrix[i][j+1]:
                    dp[i][j]=max(dp[i][j],dfs(i,j+1)+1)
                return dp[i][j]


        for i in range(m):
            for j in range(n):
                ret=max(ret,dfs(i,j))
       
        return ret+1

                
                