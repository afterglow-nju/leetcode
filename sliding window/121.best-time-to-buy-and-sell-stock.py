class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=float('inf')
        ret=0
        for i in prices:
            l=min(l,i)
            ret=max(ret,i-l)
        return ret