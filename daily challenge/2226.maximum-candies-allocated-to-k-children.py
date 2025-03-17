class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        def check(n):
            ret=0
            for i in candies:
                ret+=i//n
            return ret
        left,right=1,max(candies)
        ans=0
        while left<=right:
            mid=(right-left)//2+left
            #print(mid,check(mid))
            if check(mid)>=k:
                left=mid+1
                ans=mid
            else:
                right=mid-1
        return ans