    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<=1:
            return True
        
        intervals.sort(key=lambda x: x.start)
        prev=intervals[0]
        for i in range(1,len(intervals)):
            if prev.end>intervals[i].start:
                return False
            prev=intervals[i]
        return True
        