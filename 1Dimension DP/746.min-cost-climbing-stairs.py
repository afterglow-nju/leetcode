class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n=len(cost)
        f=[0]*(n+1)
        f[0],f[1]=cost[0],cost[1]
        cost.append(0)
        for i in range(2,n+1):
            f[i]=min(f[i-2],f[i-1])+cost[i]
        return f[n]