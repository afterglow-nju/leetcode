class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ret=[]
        for i in timePoints:
            tem=i.split(":")
            ret.append((int(tem[0]),int(tem[1])))
        ret.sort()
        ans=60*(23-ret[-1][0])+(60-ret[-1][1])+ret[0][0]*60+ret[0][1] 
        
        for i in range(1,len(ret)):
            if ret[i][0]>ret[i-1][0]:
                ans=min(ans,60-ret[i-1][1]+ret[i][1]+(ret[i][0]-1-ret[i-1][0])*60)
            else:
                ans=min(ans,-ret[i-1][1]+ret[i][1])
        return ans