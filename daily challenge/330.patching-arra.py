class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        m=0
        ret=0
        #[0,n]
        i=0
        while i<len(nums):
            if nums[i]>m+1:#[0,m] m+1 cannot be formed
                # add m+1
                ret+=1
                m+=m+1
            else:
                m+=nums[i]
                i+=1
            if m>=n:
                break
        while m<n:
            ret+=1
            m+=m+1
        return ret