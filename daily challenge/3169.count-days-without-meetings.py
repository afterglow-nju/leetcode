class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        s,e=meetings[0][0],meetings[0][1]
        new=[]
        for beg,end in meetings:
            if beg>e:
                #new.append([s,e])
                days-=(e-s+1)
                s,e=beg,end
            else:
                e=max(e,end)
        days-=(e-s+1)

        return days
