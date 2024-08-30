class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self):
                self.parent = {}  # Use a dictionary to store parent relationships
                self.rank = {}  # Dictionary to store the rank (for union by rank)

            def find(self, p):
                # If p is not in parent, it means it's a new node, so initialize it
                if p not in self.parent:
                    self.parent[p] = p
                    self.rank[p] = 1
                    return p
                # Path compression: find the root of p and compress the path
                if self.parent[p] != p:
                    self.parent[p] = self.find(self.parent[p])
                return self.parent[p]

            def union(self, p, q):
                rootP = self.find(p)
                rootQ = self.find(q)

                if rootP != rootQ:
                    # Union by rank to keep trees flat
                    if self.rank[rootP] > self.rank[rootQ]:
                        self.parent[rootQ] = rootP
                    elif self.rank[rootP] < self.rank[rootQ]:
                        self.parent[rootP] = rootQ
                    else:
                        self.parent[rootQ] = rootP
                        self.rank[rootP] += 1

            def count_components(self):
                # Use find to ensure path compression and correct root
                root_set = {self.find(p) for p in self.parent}
                return len(root_set)

        uf=UnionFind()
        for i in stones:
            uf.union(10000+i[0],i[1])
        print(len(stones),uf.count_components())
        return len(stones)-uf.count_components()
            