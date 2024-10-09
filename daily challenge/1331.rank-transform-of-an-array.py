class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(list(set(arr)))
        rank=defaultdict(int)
        for i,v in enumerate(s):
            rank[v]=i
        return [rank[i]+1 for i in arr]
