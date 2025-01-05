class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD=10**9+7
        m, n = len(words[0]),len(target)
        ans = [1]+ [0]*n
        words = list(map(Counter,zip(*map(list,words))))


        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            f[i][0] = 1
        for i in range(m):
            for j in range(n):
                f[i + 1][j + 1] = (f[i][j + 1] + words[i][target[j]] * f[i][j]) % MOD
        return f[-1][-1]



        '''
        def dfs(i,j):
            if j==-1:
                return 1
            if i==-1:
                return 0
            return (dfs(i-1,j)+words[i][target[j]]*dfs(i-1,j-1))%MOD
        
        return dfs(m-1,n-1)
        '''