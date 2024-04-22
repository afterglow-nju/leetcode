class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=dict()
        for i in nums:
            hashset[i]=hashset.get(i,0)+1
            if hashset[i]==2:
                return True
        return False