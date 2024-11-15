class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1  # 先把 n 减一，这样下面讨论的 n 就是原来的 n-1
        i = j = 0
        while n >> j:
            # x 的第 i 个比特值是 0，即「空位」
            if (x >> i & 1) == 0:
                # 空位填入 n 的第 j 个比特值
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x
