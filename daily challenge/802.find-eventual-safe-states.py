class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        ind=[0]*n
        edge=defaultdict(list)
        for i,node in enumerate(graph):
            for j in node:
                edge[j].append(i)
                ind[i]+=1
        q=deque()
        for i in range(n):
            if ind[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            for i in edge[node]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
        #print(ind)
        return [i for i in range(n) if ind[i]==0]