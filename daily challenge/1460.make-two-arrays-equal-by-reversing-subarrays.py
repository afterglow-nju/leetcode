class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        l=len(target)
        d=defaultdict(int)
        for i in target:
            d[i]+=1
        for i in arr:
            if d[i]>0:
                d[i]-=1
            else:
                return False
        return True
