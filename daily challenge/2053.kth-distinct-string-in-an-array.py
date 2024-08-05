class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=defaultdict(int)
        for i in range(len(arr)):
            d[arr[i]]+=1
        ret=[]
        for i in d:
            if d[i]==1:
                ret.append(i)
        #print(ret)
        return ret[k-1] if k-1<len(ret) else ""
        