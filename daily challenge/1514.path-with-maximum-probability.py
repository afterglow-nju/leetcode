class Solution:
    def maxProbability(self, n: int, e: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        edge=defaultdict(list)
        for i in range(len(e)):
            edge[e[i][0]].append((e[i][1],-math.log2(succProb[i])))
            edge[e[i][1]].append((e[i][0],-math.log2(succProb[i])))
        def dij(e,s):
            dis=defaultdict(lambda:float('inf'))
            dis[s]=0
            q=[(0,s)]
            vis=set()
            while q:
                _,u=heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v,w in e[u]:
                    if dis[v]>dis[u]+w:
                        dis[v]=dis[u]+w
                        heapq.heappush(q,(dis[v],v))
                #print(dis)
            return dis
        dis=dij(edge,start_node)
        #print(dis[end_node])
        return 2**-dis[end_node] if dis[end_node]!=float('inf') else 0