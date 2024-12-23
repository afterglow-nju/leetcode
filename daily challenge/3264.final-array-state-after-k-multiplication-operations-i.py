class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        ret=nums
        heap=[[nums[i],i] for i in range(len(nums))]
        heapq.heapify(heap)
        for i in range(k):
            tem=heapq.heappop(heap)
            ret[tem[1]]=tem[0]*multiplier
            heapq.heappush(heap,[tem[0]*multiplier,tem[1]])
        return ret
        