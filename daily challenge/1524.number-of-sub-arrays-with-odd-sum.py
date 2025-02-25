class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod=10**9+7
        odd=0
        even=1
        ret=0
        cnt=0

        for i in arr:
            cnt+=i
            if cnt%2==0:
                ret+=odd
                even+=1
            else:
                ret+=even
                odd+=1
        return ret%mod
            