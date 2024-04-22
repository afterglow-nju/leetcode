class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre,suf=[],[]
        tem=1
        for i,n in enumerate(nums):
            tem*=n
            pre.append(tem)
        tem=1
        for i,n in enumerate(reversed(nums)):
            tem*=n
            suf.append(tem)
        suf.reverse()
        ret=[]
              
        ret.append(suf[1])
        for i in range(1,len(nums)-1):
            ret.append(pre[i-1]*suf[i+1])
        ret.append(pre[len(nums)-2])
        return ret