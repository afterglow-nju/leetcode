class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        def dijkstra(e, s):
            """
            输入：
            e:邻接表
            s:起点
            返回：
            dis:从s到每个顶点的最短路长度
            """
            dis = defaultdict(lambda: float("inf"))
            dis[s] = 0
            q = [(0, s)]
            vis = set()
            while q:
                _, u = heapq.heappop(q)
                if u in vis:
                    continue
                vis.add(u)
                for v, w in e[u]:
                    if dis[v] > dis[u] + w:
                        dis[v] = dis[u] + w
                        heapq.heappush(q, (dis[v], v))
            return dis
        
        
        g=defaultdict(list)
        for i in times:
            g[i[0]].append((i[1],i[2]))
        dis=dijkstra(g,k)
        #print(dis)
        return max(dis.values()) if len(dis.keys())==n else -1
    
    
    
    
    
from itertools import combinations

def maximumValue(nums, k):
        n = len(nums)
        
        if 2 * k > n:
            return 0  # Edge case: Not enough elements to form a sequence of size 2 * k
    
        # Function to compute the OR of a subset
        def compute_or(subset):
            or_value = 0
            for num in subset:
                or_value |= num
            return or_value
    
        # Generate all combinations of length k
        all_combinations = list(combinations(nums, k))
        
        # Compute OR values for all k-combinations
        or_values = [compute_or(comb) for comb in all_combinations]
        
        max_xor = 0
        length = len(or_values)
        
        # Compare every pair of OR values
        for i in range(length):
            for j in range(i + 1, length):
                max_xor = max(max_xor, or_values[i] ^ or_values[j])
        
        return max_xor

# Example usage
nums = [1, 2, 3, 4, 5, 6]
k = 2
print(maximumValue(nums, k))  # Output the maximum value of the defined sequence




