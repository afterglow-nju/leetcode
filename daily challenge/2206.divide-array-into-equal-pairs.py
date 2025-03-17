class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        for v in d.values():
            if v&1==1:
                return False
        return True