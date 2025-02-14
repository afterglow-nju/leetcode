class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d=defaultdict(int)
        ret=-1
        for i in nums:
            s=sum([int(j) for j in str(i)])
            if s in d:
                ret=max(ret,d[s]+i)
                d[s]=max(d[s],i)
            else:
                d[s]=i

        return ret