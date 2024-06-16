class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        ret=0
        m=0
        for i in coins:
            if i>m+1:
                break
            m+=i
        return m+1