class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h=[-i for i in gifts]
        heapq.heapify(h)
        for i in range(k):
            v=-heapq.heappop(h)
            heapq.heappush(h,-math.floor(v**0.5))
        return -sum(h)