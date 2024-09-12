class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        tem=start^goal
        ret=0
        while tem:
            ret+=tem&1
            tem>>=1
        return ret