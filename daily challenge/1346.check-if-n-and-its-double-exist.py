class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        for i in range(len(arr)):
            x=arr[i]
            if (2*x in d and d[2*x]!=i) or (x%2==0 and x//2 in d and d[x//2]!=i):
                return True
            d[x]=i
        return False