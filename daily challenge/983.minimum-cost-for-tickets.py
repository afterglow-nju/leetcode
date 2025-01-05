class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_dat=days[-1]
        f=[0]*(last_dat+1)
        for i in range(1,last_dat+1):
            if i not in days:
                f[i]=f[i-1]
            else:
                f[i]=min(f[i-1]+costs[0],f[max(i-7,0)]+costs[1],f[max(i-30,0)]+costs[2])
        return f[-1]
        '''
        dp=[0]*(max(days))
        dp[0]=costs[0]
        for i in range(1,max(days)):
            dp[i]=dp[i-1]+costs[0]
            if i-7+1>=0:
                dp[i]=min(dp[i],dp[i-6]+costs[1])
            if i-30+1>=0:
                dp[i]=min(dp[i],dp[i-29]+costs[2])
        '''