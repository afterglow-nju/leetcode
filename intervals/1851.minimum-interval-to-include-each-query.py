class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x:x[0])
        qindex=list(range(len(queries)))
        qindex.sort(key=lambda x:queries[x])
        ret=[0]*len(queries)
        h=[]
        heapq.heapify(h)
        index=0
        for i in range(len(queries)):
            num=queries[qindex[i]]
            while index<len(intervals) and intervals[index][0] <= num:
                heapq.heappush(h,(intervals[index][1]-intervals[index][0]+1,intervals[index][1]))
                index+=1
            while h and h[0][1]<num:
                heapq.heappop(h)
            if h:
                ret[qindex[i]]=h[0][0]
            else:
                ret[qindex[i]]=-1
            
        return ret
        '''
        inter.sort(key=lambda x: x[1]-x[0]+1 )
        #queries.sort()
        ret=[]
        j=0
        for i in queries:
            f=False
            for j in inter:
                if j[0]<=i<=j[1]:
                    f=True
                    ret.append(j[1]-j[0]+1)
                    break
            if not f:
                ret.append(-1)
        return ret 
        '''
        '''
        d=defaultdict(int)
        for i in intervals:
            l=i[1]-i[0]+1
            for j in range(i[0],i[1]+1):
                if d[j]!=0:
                    d[j]=min(d[j],l)
                else:
                    d[j]=l
        ret=[]
        for i in queries:
            if d[i]==0:
                ret.append(-1)
            else:
                ret.append(d[i])
        return ret
        '''