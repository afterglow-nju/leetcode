class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        d=defaultdict(int)
        for i in arr1:
            tem=str(i)
            for j in range(len(tem)):
                d[tem[0:j+1]]=1
        print(d)
        ret=0
        for i in arr2:
            tem=str(i)
            for j in range(len(tem)-1,-1,-1):
                if tem[0:j+1] in d:
                    ret=max(ret,j+1)
                    break
        return ret