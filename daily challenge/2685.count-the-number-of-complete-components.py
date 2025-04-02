class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n
        self.count = [1] * n
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    def union(self, x, y):
        xx, yy = self.find(x), self.find(y)
        if xx == yy: return
        self.count[xx] = self.count[yy] = self.count[xx] + self.count[yy]
        if self.rank[xx] < self.rank[yy]: self.p[xx] = yy
        else: self.p[yy] = xx
        if self.rank[xx] == self.rank[yy]: self.rank[xx] += 1
    def size_of_group_that_x_is_a_part_of(self, x):
        return self.count[self.find(x)]

class Solution:
    def countCompleteComponents(self, n, edges):
        uf, counter = DSU(n), Counter()
        for x, y in edges: 
            uf.union(x, y)
            counter[x] += 1
            counter[y] += 1

        groups = set(uf.find(i) for i in range(n))

        for i in range(n):
            if uf.size_of_group_that_x_is_a_part_of(i) != counter[i] + 1:
                groups.discard(uf.find(i))

        return len(groups)