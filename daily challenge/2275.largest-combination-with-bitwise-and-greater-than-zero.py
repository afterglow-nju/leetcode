class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        d=defaultdict(int)
        for i in candidates:
            index=0
            while i:
                if i%2==1:
                    d[index]+=1
                index+=1
                i>>=1
        return max(d.values())