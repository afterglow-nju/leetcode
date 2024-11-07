class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        s=set(nums)
        ret=0
        for i in nums:
            t=i
            tem=1
            while t**2 in s:
                tem+=1
                t**=2
            ret=max(ret,tem)
        return ret if ret!=1 else -1
        '''
        d=defaultdict(int)
        nums.sort()
        ret=0
        for i in nums:
            d[i]=1
        for i in nums:
            v=i
            if d[v]==1:
                tem=1
                while d[v**2]==1:
                    tem+=1
                    v**=2
                    d[v]=0
                ret=max(ret,tem)
        return ret if ret!=1 else -1
        '''