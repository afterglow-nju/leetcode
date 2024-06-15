"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, inter: List[Interval]) -> int:
        
        ret=0
        cnt=0
        #不用管是谁的start和end
        
        start=sorted([i.start for i in inter])
        end=sorted([i.end for i in inter])
        s,t=0,0
        while s<len(inter):
            if start[s]<end[t]:
                cnt+=1
                s+=1
            else:
                t+=1
                cnt-=1
            ret=max(ret,cnt)
        
        return ret


"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, inter: List[Interval]) -> int:
        old=inter
        new=[]
        ret=0
        if len(inter)<=1:
            return len(inter)
        inter.sort(key=lambda x:x.start)
        prev=inter[0]
        while old:
            prev=old[0]
            #print(old[0].start,ret)
            for i in range(1,len(old)): 
                if prev.end>old[i].start:
                    new.append(old[i])
                else:
                    prev=old[i]
            ret+=1
            old=new
            new=[]
        return ret