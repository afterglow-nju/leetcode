class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        h=[]
        heapq.heapify(h)
        ret=1
        heapq.heappush(h,intervals[0][1])
        for i in range(1,len(intervals)):
            if intervals[i][0]>h[0]:
                heapq.heappop(h)
            else:
                ret+=1
            heapq.heappush(h,intervals[i][1])
        return ret