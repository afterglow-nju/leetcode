class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0]))
        #print(intervals)
        ret=0
        prev=intervals[0] #只需要保留一个，因为单调性+不相交
        for i in range(1,len(intervals)):
            if intervals[i][0]>=prev[1]:
                prev=intervals[i]
                continue
            else:
                ret+=1
                if intervals[i][1]<=prev[1]:
                    prev=intervals[i]
        
        return ret
        