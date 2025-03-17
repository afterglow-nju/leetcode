class Solution:
    def repairCars(self, rank: List[int], cars: int) -> int:
        def check(t):
            cnt=0
            for i in rank:
                cnt+=math.floor(math.sqrt(t/i))
                if cnt>=cars:
                    return True
            return cnt>=cars
        left,right=0,min(rank)*(cars**2)
        ret=0
        while left<=right:
            mid=(right-left)//2+left
            #print(mid,check(mid))
            if check(mid):
                ret=mid
                right=mid-1
            else:
                left=mid+1
        return ret