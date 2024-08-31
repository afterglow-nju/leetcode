class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        
        e=defaultdict(list)
        for i in edges:
           
            e[i[0]].append([i[1],i[2]])
            e[i[1]].append([i[0],i[2]])
        
        def dij(e,s,k):
            dis=defaultdict(lambda:float('inf'))
            dis[source]=0
            q=[[source,0]]
            s=set()

            while q:
                tem,d=heapq.heappop(q)
                if tem in s:
                    continue
                s.add(tem)
                for i in range(len(e[tem])):
                    if k==0:
                        nmd=e[tem][i][1]
                        if e[tem][i][1]==-1:
                            nmd=1
                    elif k==1 and e[tem][i][1]==-1 :
                        new_weight=target-original_dis[destination]+original_dis[e[tem][i][0]]-dis[tem]
                        if new_weight>=-e[tem][i][1]:
                            e[tem][i][1]=new_weight
                            nmd=e[tem][i][1]
                        else:
                            e[tem][i][1]=target
                            nmd=target
                    else:
                        nmd=e[tem][i][1]
                    
                            
                    
                        
                            
                    if dis[e[tem][i][0]]>=dis[tem]+nmd:
                        dis[e[tem][i][0]]=dis[tem]+nmd
                        heapq.heappush(q,[e[tem][i][0],dis[e[tem][i][0]]])
            return dis
        '''
        class Graph:
            def __init__(self, vertices):
                self.V = vertices        # Number of vertices
                self.edges = []          # Store edges as (u, v, weight)

            def add_edge(self, u, v, weight):
                # Add edge to the list
                self.edges.append((u, v, weight))

            def bellman_ford(self, graph, src):
                # Step 1: Initialize distances from src to all other vertices as infinite
                dist = [float('inf')] * self.V
                dist[src] = 0

                # Step 2: Relax all edges V - 1 times
                for _ in range(self.V - 1):
                    # Traverse through the graph
                    for u in graph:
                        for v, weight in graph[u]:
                            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                                dist[v] = dist[u] + weight

                # Step 3: Check for negative weight cycles
                for u in graph:
                    for v, weight in graph[u]:
                        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                            print("Graph contains a negative weight cycle")
                            return None

                return dist
        '''

        #g = Graph(len(e.keys()))
        #original_dis = g.bellman_ford(graph_data, source)
        original_dis = dij(e, source,0)
        
        if original_dis[destination]==target:
            print(">")
            for i in edges:
                if i[2]==-1:
                    i[2]=1
            return edges
        elif original_dis[destination]>target:
            return []
        else:
            #print(e[0][1])
            new_dis=dij(e,source,1)
            #print(e[0][1])
            if new_dis[destination]<target:
                return []
            else:
                
                edge_list = []
                s=set()
                for u in e.keys():
                    s.add(u)
                    for v, weight in e[u]:
                        if v not in s:
                            if weight==-1:
                                weight=10**9<<1
                            
                            edge_list.append([u, v, weight])
                        
                return edge_list








class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def dijkstra(op: int, source: int, adj_matrix: List[List[int]]) -> List[int]:
            # 朴素的 dijkstra 算法
            # adj_matrix 是一个邻接矩阵
            dist = [float("inf")] * n
            used = set()
            dist[source] = 0

            for round in range(n - 1):
                u = -1
                for i in range(n):
                    if i not in used and (u == -1 or dist[i] < dist[u]):
                        u = i
                used.add(u)
                for v in range(n):
                    if v not in used and adj_matrix[u][v] != -1:
                        if edges[adj_matrix[u][v]][2] != -1:
                            dist[v] = min(dist[v], dist[u] + edges[adj_matrix[u][v]][2])
                        else:
                            if op == 0:
                                dist[v] = min(dist[v], dist[u] + 1)
                            else:
                                modify = target - dist[u] - from_destination[v]
                                if modify > 0:
                                    dist[v] = min(dist[v], dist[u] + modify)
                                    edges[adj_matrix[u][v]][2] = modify
                                else:
                                    edges[adj_matrix[u][v]][2] = target
            return dist

        adj_matrix = [[-1] * n for _ in range(n)]
        # 邻接矩阵中存储边的下标
        for i, (u, v, w) in enumerate(edges):
            adj_matrix[u][v] = adj_matrix[v][u] = i
        
        from_destination = dijkstra(0, destination, adj_matrix)
        if from_destination[source] > target:
            return []
        from_source = dijkstra(1, source, adj_matrix)
        if from_source[destination] != target:
            return []
        return edges

