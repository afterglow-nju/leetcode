class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d=defaultdict(int)
        for i in dictionary:
            d[i]+=1
        s='#'+s
        dp=[float('inf')]*(len(s))
        dp[0]=0
        for i in range(1,len(s)):
            dp[i]=dp[i-1]+1
            for j in range(1,i+1):
                if s[j:i+1] in d:
                    dp[i]=min(dp[i],dp[j-1])
        return dp[-1]