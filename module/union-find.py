class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size  # Initialize size of each set to 1

    def find(self, p): #就是找到点p的根，根的性质是parent[i]=i
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