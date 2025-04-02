class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ret = []
        d=defaultdict()
        quer=sorted(queries)
        t=0
        q = [[grid[0][0],0, 0]]
        vis=set()
        vis.add((0,0))
        for k in quer:
            
            while q and q[0][0]<k:
                v,i, j = heapq.heappop(q)
                t += 1
                for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        key = (ni,nj)
                        if key not in vis:
                            vis.add(key)
                            heapq.heappush(q,[grid[ni][nj],ni,nj])
                #print(k,q)
            d[k]=t
        return [d[i] for i in queries]