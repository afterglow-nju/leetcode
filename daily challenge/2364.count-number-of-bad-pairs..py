class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n=len(nums)
        d=defaultdict(int)
        for i in range(n):
            d[nums[i]-i]+=1
        ret=(1+n-1)*(n-1)//2
        #print(ret)
        for v in d.values():
            if v>1:
                ret-=(1+v-1)*(v-1)//2
        return ret
    