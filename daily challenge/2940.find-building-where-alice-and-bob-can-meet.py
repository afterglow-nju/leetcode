class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        
        n=len(heights)
        ret=[-1]*len(queries)
        defer = [[] for _ in range(n)]
        for i,q in enumerate(queries):
            if q[0]>q[1]:
                q[0],q[1]=q[1],q[0]
            if heights[q[0]]<heights[q[1]] or q[0]==q[1]:
                ret[i]=q[1]
            else:
                defer[q[1]].append([heights[q[0]],i])
        hq=[]
        for i in range(n):
            for q in defer[i]:
                heapq.heappush(hq,q)
            while hq and hq[0][0]<heights[i]:
                ret[hq[0][1]]=i
                heapq.heappop(hq)
        return ret











        '''
        res, idx = [0] * len(queries), []
        for i, q in enumerate(queries):
            a, b = sorted(q)
            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                idx.append((a, b, i))
        j, mono = len(heights) - 1, deque()
        for a, b, i in sorted(idx, key=itemgetter(1), reverse=True):
            while j > b:
                while mono and heights[mono[0]] < heights[j]:
                    mono.popleft()
                mono.appendleft(j)
                j -= 1
            k = bisect_right(mono, heights[a], key=lambda x: heights[x])
            res[i] = -1 if k == len(mono) else mono[k]
        return res
        '''