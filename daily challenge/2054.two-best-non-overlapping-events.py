class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        h=[]
        ret=max(i[2] for i in events)
        prev=0
        for i in events:

            while h and h[0][0]<i[0]:
                prev=max(prev,heapq.heappop(h)[1])
            ret=max(ret,prev+i[2])
            heapq.heappush(h,[i[1],i[2]])
        return ret