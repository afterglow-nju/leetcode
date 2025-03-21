class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        flip = 0  # 当前位置的反转次数
        diff = [0] * (n + 3)  # 记录每个位置的反转次数
        for i in range(n):
            flip += diff[i]
            if (nums[i] ^ (flip & 1)) == 0:  # 当前位置是0，需要反转
                if i + 3 > n:  # 越界
                    return -1
                ans += 1
                flip += 1  # 增加反转次数
                diff[i + 3] -= 1  # 终止位置-1
        return ans
