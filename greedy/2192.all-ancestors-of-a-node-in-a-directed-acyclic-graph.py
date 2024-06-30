class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        ret=[set() for _ in range(n)]
        e=[[] for _ in range(n)]
        whe=[False]*n
        for i in edges:
            #print(i[1],i[0],n,e[i[1]])
            e[i[1]].append(i[0])
        
        def bfs(node):
            for i in e[node]:
                ret[node].add(i)
                if whe[i]==False:
                    ret[node]|=bfs(i)
                else:
                    ret[node]|=ret[i]
            whe[node]=True
            return ret[node]
        
        for i in range(n):
            bfs(i)
        
        return [sorted(list(i)) for i in ret]