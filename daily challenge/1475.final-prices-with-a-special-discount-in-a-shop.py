class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 单调栈，保持升序
        p=[]
        ret=[prices[-1]]
        p.append(prices[-1])
        for i in range(len(prices)-2,-1,-1):
            value=prices[i]
            while p and value<p[-1]:
                p.pop()
            if not p:
                ret.append(value)
            else:
                ret.append(value-p[-1])
            p.append(value)
        return ret[::-1]

