class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d=Counter(nums)
        ret=0
        for i in nums:
            d[i]-=1
            ret+=d[i+k]+d[i-k]
        return ret