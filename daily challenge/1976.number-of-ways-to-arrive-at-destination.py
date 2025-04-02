class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=10**9+7
        e=defaultdict(list)
        for x,y,t in roads:
            e[x].append([y,t])
            e[y].append([x,t])
        dis=[inf]*(n+1)
        ways=[0]*(n+1)
        dis[0]=0
        ways[0]=1
        q=[[0,0]]
        while q:
            t,u=heapq.heappop(q)
            if t>dis[u]:
                continue
            for v,w in e[u]:
                if t+w<dis[v]:
                    dis[v]=t+w
                    ways[v]=ways[u]
                    heapq.heappush(q,[t+w,v])
                elif t+w==dis[v]:
                    ways[v]=(ways[v]+ways[u])%mod
        return ways[n-1]