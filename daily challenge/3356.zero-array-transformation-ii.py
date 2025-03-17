class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        def check(k):#0-n
            diff=[0]*(len(nums)+1)
            for i in queries[:k]:
                diff[i[0]]+=i[2]
                diff[i[1]+1]-=i[2]
            for x,s in zip(nums,accumulate(diff)):
                if x<=s:
                    continue
                else:
                    return False
            return True
        left,right=0,len(queries)+1
        ret=-1
        while left<=right:
            mid=(right-left)//2+left
            if check(mid):
                ret=mid
                right=mid-1
            else:
                left=mid+1
        return ret