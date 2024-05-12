class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ret=[]
        heap=[]
        heapq.heapify(heap)
        d=defaultdict(list)
        for i in points:
            t=i[0]**2+i[1]**2
            heapq.heappush(heap,-t)
            #tem=heapq.heappop(heap)
            #print(-t)
            d[-t].append(i)
                
            if len(heap)>k:
                heapq.heappop(heap)
        prev=1
        while heap:
            if prev==heap[0]:
                heapq.heappop(heap)
                continue
            prev=heapq.heappop(heap)
            ret+=d[prev]
            
        return ret
        #排序也是nlogn，插入最坏也是nlog，用堆这不傻逼嘛