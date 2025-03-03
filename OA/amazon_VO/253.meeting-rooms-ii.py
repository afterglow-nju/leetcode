class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        ret=0
        while len(intervals)>0:
            n=len(intervals)
            end=0
            tem=[]
            for i in range(n):
                if intervals[i][0]>=end:
                    end=intervals[i][1]
                else:
                    tem.append(intervals[i])
            intervals=tem
            ret+=1
        return ret