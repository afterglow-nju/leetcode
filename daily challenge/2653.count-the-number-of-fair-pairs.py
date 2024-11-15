class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, j+1, len(nums))  # <= upper-nums[j] 的 nums[i] 的个数
            l = bisect_left(nums, lower - x, j+1,len(nums))  # < lower-nums[j] 的 nums[i] 的个数
            ans += r - l
        return ans
