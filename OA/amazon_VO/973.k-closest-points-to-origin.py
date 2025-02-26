class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h=[]
        for i in range(len(points)):
            x,y=points[i][0],points[i][1]
            t=x**2+y**2
            if len(h)==k:
                heapq.heappush(h,[-t,i])
                heapq.heappop(h)
            else:
                heapq.heappush(h,[-t,i])
        ret=[]
        
        while h:
            n=heapq.heappop(h)
            ret.append(points[n[1]])
            
        return ret