class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        tem=[times[i]+[i] for i in range(len(times))]
        tem.sort()
        h=[]
        index=[i for i in range(0,len(times))]
        heapq.heapify(h)
        heapq.heapify(index)
        for i in range(0,len(times)):
            
            while h and tem[i][0]>=h[0][0]:
                heapq.heappush(index,h[0][1])
                heapq.heappop(h)
            
            if tem[i][2]==targetFriend:
                return index[0]
            heapq.heappush(h,[tem[i][1],heapq.heappop(index)])
            #print(h,tem[i][1])
        assert(0)
            
        