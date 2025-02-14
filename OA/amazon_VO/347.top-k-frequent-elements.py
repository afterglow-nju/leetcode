class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        h=[]
        ret=[]
        for key,value in c.items():
            if len(h)<k:
                heapq.heappush(h,[value,key])
            else:
                if h[0][0]<value:
                    heapq.heappop(h)
                    heapq.heappush(h,[value,key])
        while h:
            t=heapq.heappop(h)
            ret.append(t[1])
        return ret