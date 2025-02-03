class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # 统计入度，便于进行拓扑排序
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1
        
        used = [False] * n
        f = [1] * n
        q = deque(i for i in range(n) if indeg[i] == 0)
        
        while q:
            u = q.popleft()
            used[u] = True
            v = favorite[u]
            # 状态转移
            f[v] = max(f[v], f[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
        
        # ring 表示最大的环的大小
        # total 表示所有环大小为 2 的「基环内向树」上的最长的「双向游走」路径之和
        ring = total = 0
        for i in range(n):
            if not used[i]:
                j = favorite[i]
                # favorite[favorite[i]] = i 说明环的大小为 2
                if favorite[j] == i:
                    total += f[i] + f[j]
                    used[i] = used[j] = True
                # 否则环的大小至少为 3，我们需要找出环
                else:
                    u = i
                    cnt = 0
                    while True:
                        cnt += 1
                        u = favorite[u]
                        used[u] = True
                        if u == i:
                            break
                    ring = max(ring, cnt)
        
        return max(ring, total)
