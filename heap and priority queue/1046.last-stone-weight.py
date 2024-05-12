class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s=[i*-1 for i in stones]
        heapq.heapify(s)
        while len(s)>1:
            a=heapq.heappop(s)
            b=heapq.heappop(s)
            t=-abs(a-b)
            if t!=0:
                heapq.heappush(s,t)
        return 0 if not s else -s[0]
