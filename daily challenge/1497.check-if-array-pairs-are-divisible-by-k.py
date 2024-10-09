class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d=defaultdict(lambda:0)
        for i in arr:
            d[i%k]+=1

        for i in range(1,k):
            if d[i]==d[k-i]:
                continue
            else:
                return False
        return d[0]%2==0