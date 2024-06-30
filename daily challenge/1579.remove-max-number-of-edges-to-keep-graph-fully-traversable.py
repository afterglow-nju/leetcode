class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.size = [1] * size  # Initialize size of each set to 1

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP != rootQ:
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


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1=UnionFind(n+1)
        uf2=UnionFind(n+1)
        uf3=UnionFind(n+1)
        r=[0,0,0]
        s=[0,0,0]
        for i in edges:
            if i[0]==1:
                s[0]+=1
                #if connected(i[1],i[2]):
                #    uf1.union(i[1],i[2])
                #else:
                #    r[0]+=1
            elif i[0]==2:
                s[1]+=1
                #if connected(i[1],i[2]):
                #    uf2.union(i[1],i[2])
                #else:
                #    r[1]+=1
            else:
                s[2]+=1
                if not uf3.connected(i[1],i[2]):
                    uf3.union(i[1],i[2])
                else:
                    r[2]+=1
        if uf3.get_size(edges[0][1])==n:
            return s[0]+s[1]+r[2]
        else:
            import copy
            t=copy.deepcopy(uf3)
            for i in edges:
                if i[0]==1:
                    if not uf3.connected(i[1],i[2]):
                        uf3.union(i[1],i[2])
                    else:
                        r[0]+=1
            if uf3.get_size(edges[0][1])==n:
                for i in edges:
                    if i[0]==2:
                        if not t.connected(i[1],i[2]):
                            t.union(i[1],i[2])
                        else:
                            r[1]+=1
                if t.get_size(edges[0][1])==n:
                    return r[1]+r[0]+r[2]
                else:
                    return -1
            else:
                return -1
        