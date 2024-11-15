class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def decide(k):
            ret=0
            for i in quantities:
                ret+=math.ceil(i/k)
            return ret<=n
        left,right=1,max(quantities)
        while left<=right:
            mid=(right-left)//2+left
            #print(left,right,mid,decide(mid))
            if decide(mid):
                right=mid-1
            else:
                left=mid+1
                
        return left