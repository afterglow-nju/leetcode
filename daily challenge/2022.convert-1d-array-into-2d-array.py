class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        ret,tem=[],[]
        for i in range(len(original)):
            tem.append(original[i])
            if (i+1)%n==0:
                ret.append(tem)
                tem=[]
        return ret