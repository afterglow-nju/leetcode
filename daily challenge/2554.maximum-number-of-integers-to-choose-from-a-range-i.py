class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        r=list(set(list(range(1,n+1)))-set(banned))
        r.sort()
        ret=0
        tem=0
        for i in r:
            tem+=i
            if tem<=maxSum:
                ret+=1
            else:
                break
        return ret