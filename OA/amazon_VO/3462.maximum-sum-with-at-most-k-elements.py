class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        h=[]
        if k==0:
            return 0
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(min(len(grid[i]),limits[i])):
                if len(h)<k:
                    heapq.heappush(h,grid[i][j])
                else:
                    if grid[i][j]>h[0]:
                        heapq.heappop(h)
                        heapq.heappush(h,grid[i][j])
                    else:
                        break
        return sum(h)

        