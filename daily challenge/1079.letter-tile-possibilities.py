class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = Counter(tiles).values()  # 统计每个字母的出现次数
        n, m = len(tiles), len(counts)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][0] = 1  # 构造空序列的方案数
        for i, cnt in enumerate(counts, 1):  # 枚举第 i 种字母
            for j in range(n + 1):  # 枚举序列长度 j
                for k in range(min(j, cnt) + 1):  # 枚举第 i 种字母选了 k 个
                    f[i][j] += f[i - 1][j - k] * comb(j, k)  # comb 也可以预处理，见其它语言
        return sum(f[m][1:])
