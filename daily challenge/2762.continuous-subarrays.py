class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        cnt=Counter()
        ret=0
        left=0
        for right,x in enumerate(nums):
            cnt[x]+=1
            while max(cnt)-min(cnt)>2:
                y=nums[left]
                cnt[y]-=1
                if cnt[y]==0:
                    del cnt[y]
                left+=1
            ret+=right-left+1
        return ret