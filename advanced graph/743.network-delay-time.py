class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
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
        
        
        g=defaultdict(list)
        for i in times:
            g[i[0]].append((i[1],i[2]))
        dis=dijkstra(g,k)
        #print(dis)
        return max(dis.values()) if len(dis.keys())==n else -1