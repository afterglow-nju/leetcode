class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:      
        #p=[i+values[i] for i in range(len(values))]
        #m=[-i+values[i] for i in range(len(values))]
        ret=0
        max_left=values[0]
        for i in range(1,len(values)):
            ret=max(max_left+values[i]-i,ret)
            max_left=max(max_left,i+values[i])
        return ret