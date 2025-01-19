class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s=set()
        ret=[]

        for i in range(len(A)):
            s.add(A[i])
            s.add(B[i])
            ret.append((i+1)*2-len(s))
        return ret