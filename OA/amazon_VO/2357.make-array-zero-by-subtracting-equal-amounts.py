class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s=set(nums)
        s.add(0)
        s.remove(0)
        return len(s)