class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def helper(beg: int, end: int, cnt = 0) -> bool:

            order = sorted(range(m), key = lambda x: beg[x])
            acc = end[order.pop(0)]

            for i in order:
                if acc <= beg[i]: cnt+= 1
                if cnt >= 2: return True
                if acc <= end[i]: acc = end[i]
            return False

        m = len(rectangles)
        x_beg, y_beg, x_end, y_end  = map(list, zip(*rectangles))

        if helper(x_beg, x_end): return True
        return helper(y_beg, y_end)