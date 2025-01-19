class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        def dijkstra(e, s):
            """
            输入：
            e:邻接表
            s:起点
            返回：
            dis:从s到每个顶点的最短路长度
            """
            dis = defaultdict(lambda: float("inf"))
            dis[s] = 0
            q = [(0, s)]
            vis = set()
            while q:
                _, u = heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v, w in e[u]:
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            return dis
        
        g=defaultdict(lambda:[])
        m,n=len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                w1,w2,w3,w4=1,1,1,1
                if grid[i][j]==1:
                    w1=0
                if grid[i][j]==2:
                    w2=0
                if grid[i][j]==3:
                    w3=0
                if grid[i][j]==4:
                    w4=0
                    
                if j+1<n:
                    g[i*n+j].append((i*n+j+1,w1))
                if j-1>=0:
                    g[i*n+j].append((i*n+j-1,w2))
                if i+1<m:
                    g[i*n+j].append(((1+i)*n+j,w3))
                if i-1>=0:
                    g[i*n+j].append(((i-1)*n+j,w4))
        dis=dijkstra(g,0)
        #print(len(dis),dis)
        #assert(len(dis)==m*n)
        return dis[m*n-1]
