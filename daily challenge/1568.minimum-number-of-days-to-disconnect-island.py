class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        # 先用并查集看有多少个连通块，若不等于1，返回0
        # 若等于1，tarjan算法求割点，若不存在，返回2，反之返回1
        m = len(grid)
        n = len(grid[0])
        fa = list(range(m * n))

        def find(x_: int) -> int:
            if fa[x_] != x_:
                fa[x_] = find(fa[x_])
            return fa[x_]

        g = [[] for _ in range(m * n)]
        vis = [[0] * n for _ in range(m)]
        cc = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 0 or vis[i][j] == 1:
                    continue
                cur = [(i, j)]
                vis[i][j] = 1
                while cur:
                    pre = cur
                    cur = []
                    for x0, y0 in pre:
                        cc += 1
                        x = x0 * n + y0
                        fx = find(x)
                        for x1, y1 in (x0 + 1, y0), (x0 - 1, y0), (x0, y0 + 1), (x0, y0 - 1):
                            if 0 <= x1 < m and 0 <= y1 < n and vis[x1][y1] == 0 and grid[x1][y1] == 1:
                                y = x1 * n + y1
                                g[x].append(y)
                                g[y].append(x)
                                fy = find(y)
                                fa[fy] = fx
                                cur.append((x1, y1))
                    cur = list(set(cur))
                    for x, y in cur:
                        vis[x][y] = 1

        st = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    st.add(find(i * n + j))
        if len(st) != 1:
            return 0
        if cc == 1:
            return 1
        # tarjan
        t = TARJAN(m*n, g)
        t.tarjan(list(st)[0], -1, 0)
        return 1 if any(x for x in t.flag) else 2


class TARJAN:
    def __init__(self, n: int, g: List[List[int]]):
        # 记录结点的当前时间戳和最早时间戳,从根开始的一条路径上dfn 严格递增，low 严格非降
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.bridge = []  # 桥
        self.flag = [False] * n  # 是否是割点
        self.g = g

    def tarjan(self, o: int, f: int, t: int) -> None:
        self.dfn[o] = t
        self.low[o] = t
        c = 0
        for child in self.g[o]:
            if child != f:
                if self.dfn[child] == -1:
                    c += 1
                    self.tarjan(child, o, t + 1)
                    self.low[o] = min(self.low[o], self.low[child])
                    # 找到割点, 非root,有儿子
                    if self.dfn[o] <= self.low[child] and f != -1 and not self.flag[o]:
                        self.flag[o] = True
                    # 找到桥
                    if self.dfn[o] < self.low[child]:
                        self.bridge.append([o, child])
                else:
                    self.low[o] = min(self.low[o], self.dfn[child])
        # root点 儿子数大于等于2
        if f == -1 and c >= 2 and not self.flag[o]:
            self.flag[o] = True

'''
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [0] * size
                self.size = [1] * size  # Initialize size of each set to 1

            def find(self, p): #就是找到点p的根，根的性质是parent[i]=i
                #print(p)
                if self.parent[p] != p:
                    self.parent[p] = self.find(self.parent[p])  # Path compression
                return self.parent[p]

            def union(self, p, q):
                rootP = self.find(p)
                rootQ = self.find(q)

                if rootP != rootQ: #优先往rank小的树上合并，这样find递归次数少
                    # Union by rank
                    if self.rank[rootP] > self.rank[rootQ]:
                        self.parent[rootQ] = rootP
                        self.size[rootP] += self.size[rootQ]  # Update size
                    elif self.rank[rootP] < self.rank[rootQ]:
                        self.parent[rootP] = rootQ
                        self.size[rootQ] += self.size[rootP]  # Update size
                    else:
                        self.parent[rootQ] = rootP
                        self.size[rootP] += self.size[rootQ]  # Update size
                        self.rank[rootP] += 1

            def connected(self, p, q):
                return self.find(p) == self.find(q)

            def get_size(self, p):
                rootP = self.find(p)
                return self.size[rootP]

            def count_components(self):
                root_set = set(self.find(i) for i in range(len(self.parent)))
                return len(root_set)

        m,n=len(grid),len(grid[0])
        uf=UnionFind(m*n+1)
        bridge=0
        total=sum(sum(grid[i]) for i in range(m))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    X,Y=0,0
                    if j<n-1 and grid[i][j+1]==1:
                        Y+=1
                    if i<m-1 and grid[i+1][j]==1:
                        X+=1
                
                    if i>0 and grid[i-1][j]==1:
                        uf.union(i*n+j,(i-1)*n+(j))
                        X+=1
                    if j>0 and grid[i][j-1]==1:
                        uf.union(i*n+j,(i)*n+(j-1))
                        Y+=1
                    if (Y==0 and X==2) or (X==0 and Y==2):
                        print(i,j)
                        bridge+=1
        size=uf.count_components()-1
        print(size)
        if 1+m*n-total!=size:
            return 0
        else:   
            print(bridge)    
            if bridge==1:
                return 1
            else:
                return 2
'''