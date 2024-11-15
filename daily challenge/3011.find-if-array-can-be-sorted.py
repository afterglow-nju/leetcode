class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def one(num):
            ret=0
            while num:
                if num&1==1:
                    ret+=1
                num>>=1
            return ret
        
        prev,now=[],[]
        cnt=one(nums[0])
        for i in nums:
            tem=one(i)
            if cnt==tem:
                now.append(i)
            else:
                cnt=tem
                if not prev or max(prev)<=min(now):
                    prev=now
                    now=[i]
                else:
                    return False
        if not prev or max(prev)<=min(now):
            return True
        else:
            return False