class Solution:
    

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        class unionfind:
            def __init__(self,size):
                self.parent=list(range(size))
                self.rank=[0]*size
                self.size=[1]*size
                self.total=size
            def find(self,p):
                while p!=self.parent[p]:
                    p=self.parent[p]
                return p
            def union(self,p,q):
                p1,p2=self.find(p),self.find(q)
                if p1!=p2:
                    self.total-=1
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
        
        uf=unionfind(n)
        for i in edges:
            uf.union(i[0],i[1])
        
        return uf.total