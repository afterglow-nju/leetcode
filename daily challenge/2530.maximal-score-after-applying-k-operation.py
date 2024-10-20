class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h=[-i for i in nums]
        heapq.heapify(h)
        ret=0
        for i in range(k):
            t=heapq.heappop(h)
            #print(-t)
            ret+=-t
            heapq.heappush(h,-ceil(-t/3))
        return ret