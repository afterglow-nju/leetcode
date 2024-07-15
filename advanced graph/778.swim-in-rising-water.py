class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        n=len(grid)

        visit=[[False]*n for _ in range(n)]
        visit[0][0]=True
        heap=[(grid[0][0],0,0)]
        ret=0
        while True:
            i,j=heap[0][1],heap[0][2]
            #print(i,j,heap[0][0])
            ret=max(ret,heap[0][0])
            heapq.heappop(heap)
            if i==n-1 and j==n-1:
                return ret
                

            for k in d:
                if 0<=k[0]+i<n and 0<=k[1]+j<n:
                    if visit[k[0]+i][k[1]+j]==False:
                        #print("!",k[0]+i,k[1]+j,grid[k[0]+i][k[1]+j])
                        visit[k[0]+i][k[1]+j]=True
                        heapq.heappush(heap,(grid[k[0]+i][k[1]+j],k[0]+i,k[1]+j))
        

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        def dijkstra(e, s,time):
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

                    if w<=time:
                        w=0

                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            return dis
        g=defaultdict(set)
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        n=len(grid)
        for i in range(n):
            for j in range(n):
                node=i*n+j
                for k in d:
                    if 0<=k[0]+i<n and 0<=k[1]+j<n:
                        g[node].add(((k[0]+i)*n+k[1]+j,grid[k[0]+i][k[1]+j]))
                        #print(g[0],k[0],k[1],i,j)
                        g[(k[0]+i)*n+k[1]+j].add((node,grid[i][j]))
        
        #print(g)
        
        left=max(grid[0][0],grid[n-1][n-1])
        right=n**2
        mid=(right-left)//2+left
        while left<=right:
            mid=(right-left)//2+left
            ret=dijkstra(g,0,mid)
            #print(ret)
            if ret[n**2-1]==0:
                right=mid-1
            else:
                left=mid+1
        return left
        '''
        left=max(grid[0][0],grid[n-1][n-1])
        while True:
            ret=dijkstra(g,0,left)
            #print(left,ret)
            if ret[n**2-1]==0:
                return left
            else:
                left+=1
        '''
        