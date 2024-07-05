class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.rank = [0] * n  # 初始情况下，每个节点的 rank 为 0

            def find(self, p):
                if self.parent[p] != p:
                    self.parent[p] = self.find(self.parent[p])  # 路径压缩
                return self.parent[p]

            def union(self, p, q):
                rootP = self.find(p)
                rootQ = self.find(q)

                if rootP != rootQ:
                    if self.rank[rootP] > self.rank[rootQ]:
                        self.parent[rootQ] = rootP
                    elif self.rank[rootP] < self.rank[rootQ]:
                        self.parent[rootP] = rootQ
                    else:
                        self.parent[rootQ] = rootP
                        self.rank[rootP] += 1  # 如果两个 rank 相同，新的根的 rank 增加 1

            def connected(self, p, q):
                return self.find(p) == self.find(q)
        
        uf=UnionFind(len(edges)+1)
        for i in edges:
            if not uf.connected(i[0],i[1]):
                uf.union(i[0],i[1])
            else:
                return i
        assert(0)