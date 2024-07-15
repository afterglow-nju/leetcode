class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        graph = defaultdict(list)
        for j in range(1,len(points)):
            d = abs(points[0][0] - points[j][0]) + abs(
                points[0][1] - points[j][1]
            )
            graph[0].append((d, 0, j))
                    
        visit = [0] * len(points)
        visit[0] = 1
        minheap = graph[0]
        heapq.heapify(minheap)
        ret = 0
        while minheap:
            t = heapq.heappop(minheap)

            if visit[t[2]] == 1:
                continue
            visit[t[2]] = 1
            #print(t[0])
            ret += t[0]

            for j in range(len(points)):
                if t[2] != j and visit[j]==0:
                    d = abs(points[t[2]][0] - points[j][0]) + abs(
                        points[t[2]][1] - points[j][1]
                    )
                    graph[t[2]].append((d, t[2], j))

            for i in graph[t[2]]:
                if visit[i[2]] == 0:
                    heapq.heappush(minheap, i)
        return ret

        """
        class unionfind:
            def __init__(self,size):
                self.parent=list(range(size))
                self.size=[0]*size    
            
            def find(self,x):
                while self.parent[x]!=x:
                    x=self.find(self.parent[x])
                return x

            def union(self,x,y):
                p1,p2=self.find(x),self.find(y)
                if p1!=p2:
                    self.parent[p1]=p2
                    self.size[p2]+=self.size[p1]

            def get_size(self,x):
                p=self.find(x)
                return self.size[p]

        uf=unionfind(len(points))
        edge=[]
        for i in range(len(points)):
            for j in range(len(points)):
                if i!=j:
                    d=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    edge.append((d,i,j))
                    edge.append((d,j,i))
        edge.sort()
        ret=0
        for i in range(len(edge)):
            e=edge[i]
            if uf.find(e[1])!=uf.find(e[2]):
                #print(e)
                uf.union(e[1],e[2])
                ret+=e[0]
                if uf.get_size(e[1])==len(points):
                    break
        return ret
        """
