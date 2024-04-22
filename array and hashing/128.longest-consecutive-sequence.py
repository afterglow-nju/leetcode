from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        ret=0
        for i in nums:
            l=1
            if i-1 not in nums:
                while i+l in nums:
                    l+=1
                ret=max(ret,l)
        return ret
    
        '''
        d=defaultdict(int)
        #d[i] stands for the longest consecutive element that contains i
        ret=0
        for i in set(nums):
            #if d[i]!=0:
            #    continue
            d[i]=1+d[i-1]+d[i+1]
            d[i+d[i+1]]=d[i]
            d[i-d[i-1]]=d[i]
            ret=max(ret,d[i])
        return ret
        '''