class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0
        def dfs(x: int, fa: int) -> int:
            s = values[x]
            for y in g[x]:
                if y != fa:
                    s += dfs(y, x)
            nonlocal ans
            ans += s % k == 0
            return s
        dfs(0, -1)
        return ans


class Solution:
    def maxKDivisibleComponents(self, n, edges, value, k) -> int:

        if n <= 1 : return 1
        
        ret = 0

        # build adjacency map
        G = defaultdict(lambda:[])
        for u,v in edges: 
            G[u].append(v)
            G[v].append(u)

        Q=deque()
        for key,v in G.items():
            if len(v)==1:
                Q.append(key)

        vis=[False]*len(value)
        while Q:
            for _ in range(len(Q)):
                node=Q.popleft()
                if vis[node]:
                    continue
                vis[node]=True
                
                #print(node,G[node])

                #assert(len(G[node])<=1)

                if len(G[node])==0:
                    ret+=1
                    continue

                parent=G[node][0]
                if value[node]%k==0:
                    ret+=1
                else:
                    value[parent]+=value[node]
                G[parent].remove(node)
                if len(G[parent])==1:
                    Q.append(parent)
        return ret










        '''
        # start with leaves
        Q = deque(u for u, vs in G.items() if len(vs) == 1)
        
        # cut leaves layer by layer
        while Q:
            for _ in range(len(Q)):
                u = Q.popleft()
                
                # get u's parent and remove u from its children
                p = next(iter(G[u])) if G[u] else -1
                if p >= 0 : G[p].remove(u)
                
                # either separate a correct component or add to parent
                if values[u] % k == 0 : count += 1
                else                  : values[p] += values[u]

                # update queue with new leaves
                if p >= 0 and len(G[p]) == 1 : Q.append(p)

        return count
        '''