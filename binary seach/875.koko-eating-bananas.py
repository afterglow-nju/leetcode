#大概率这样，两种算法想法一致，但我写的比较繁琐，但是我效率反而高 :joy:

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        left=1
        right=max(piles)
        k=0
        label=False
        while left<=right:
            mid=(right-left)//2+left
            k=mid
            ret=0
            for i in piles:
                #print(math.ceil(i/k))
                ret+=math.ceil(i/k)
            if ret>h:
            #    assert(0)
                print("a")
                left=mid+1
                label=True
            elif ret<=h:
            #    assert(0)
                print('b')
                right=mid-1
                label=False
            #else:
            #    assert(0)
            #    print(k)
            #    return k
        print(left,right,k)
        if label:
            return k+1
        return k
        assert(0)

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        k=right
        while left<=right:
            mid=(right-left)//2+left
            ret=0
            for i in piles:
                ret+=math.ceil(i/mid)
            if ret>h:
                left=mid+1
            elif ret<=h:
                right=mid-1
                k=min(k,mid)
        return k
        assert(0)