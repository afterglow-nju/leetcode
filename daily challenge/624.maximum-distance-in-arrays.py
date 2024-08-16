class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans=[]
        Min,Max=arrays[0][0],arrays[0][-1]
        Dif=float('-inf')
        for i in arrays[1:]:
            Dif=max(Dif,abs(Max-i[0]),abs(i[-1]-Min))
            Min=min(Min,i[0])
            Max=max(Max,i[-1])
        return Dif