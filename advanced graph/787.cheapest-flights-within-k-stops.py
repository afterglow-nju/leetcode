class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        g=defaultdict(list)
        for i in flights:
            g[i[0]].append((i[1],i[2]))
        heap=[[0,0,src]] # node cost times
        #visit=[float('inf')]*n
        visit=[n+1]*n
        ret=float('inf')
        while heap:
            cost,step,node=heapq.heappop(heap)
            #print(heap,cost,step,node,visit[node])
            if node==dst:
                return cost
                #print(cost)
                #ret=min(ret,cost)
                #continue
            if step>k or step>=visit[node] :#cost>=visit[node]:# 如果是cost，就会导致为了cost小而走近路，不绕远
                continue
            visit[node]=step#cost#
            for i in g[node]:
                heapq.heappush(heap,[cost+i[1],step+1,i[0]])

        return ret if ret!=float('inf') else -1

        '''
        q=deque()
        g=defaultdict(list)
        for i in flights:
            g[i[0]].append((i[1],i[2]))
        dist=[[float('inf'),float('inf')] for _ in range(n)]
        dist[0][0]=0
        dist[0][1]=0
        q.append((src,0)) # node dis level
        ret=float('inf')

        while q:
            node,level=q.pop()
            #if node==dst:
            #    ret=min(ret,dist[node][0])
                

            #if level<=k:
            for i in g[node]:
                #print(node,i[0],dist[i[0]])
                if i[1]+dist[node][0]<dist[i[0]][0] and level<=k:# and dist[i[0]][1]+1<=k+1:#level+1<=k+1:#dist[i[0]][1]:
                    
                    q.append((i[0],level+1))
                    dist[i[0]][0]=i[1]+dist[node][0]
                    dist[i[0]][1]=level+1
                    print(node,i[0],dist[i[0]])
        
        return dist[dst][0] if dist[dst][0]!=float('inf') else -1
        '''
        '''
        def dfs(node,level,d):
            #print(node,level,d)

            ret=float('inf')
            if level<=k+1:
                if node==dst:
                    ret=d
            else:
                return float('inf')
            
            for i in g[node]:
                ret=min(ret,dfs(i[0],level+1,d+i[1]))
            return ret
        ans=dfs(src,0,0)
        #print(ans)
        return ans if ans!=float('inf') else -1
        '''