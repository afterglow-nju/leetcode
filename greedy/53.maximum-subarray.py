#遍历是只有两种选择，加入或重新开始
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret=float('-inf')
        tem=0
        for i in nums:
            tem+=i
            ret=max(ret,tem)
            if tem<0:
                tem=0
        return ret