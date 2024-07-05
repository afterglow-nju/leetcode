class Solution:
     class unionfind:
            def __init__(self,size):
                self.parent=list(range(size))
                self.rank=[0]*size
                self.size=[1]*size
            def find(self,p):
                while p!=self.parent[p]:
                    p=self.parent[p]
                return p
            def union(self,p,q):
                p1,p2=self.find(p),self.find(q)
                if p1!=p2:
                    if self.rank[p1]<self.rank[p2]:
                        self.parent[p2]=p1
                        self.size[p1]+=self.size[p2]
                    elif self.rank[p2]<self.rank[p1]:
                        self.parent[p1]=p2
                        self.size[p2]+=self.size[p1]
                    else:
                        self.parent[p1]=p2
                        self.rank[p2]+=1
                        self.size[p2]+=self.size[p1]
            def connect(self,p,q):
                return self.find(p)==self.find(q)
            def get_size(self,p):
                return self.size[self.find(p)]
            
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf=unionfind(n)
        for i in edges:
            if uf.find(i[0])!=uf.find(i[1]):
                uf.union(i[0],i[1])
            else:
                return False
        return (n==1 and edges==[]) or uf.get_size(edges[0][0])==n