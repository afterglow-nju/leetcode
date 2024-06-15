




class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        ret=[]
        t=[-1,-1]
        i=0
        while i <len(intervals):
            if intervals[i][0]<=new[0]<=intervals[i][1]:
                t[0]=intervals[i][0]
                #print("A")
                while True and i<len(intervals):
                    
                    if new[1]<intervals[i][0]:
                        t[1]=new[1]
                        ret.append(t)
                        break
                    elif new[1]<=intervals[i][1]:
                        t[1]=intervals[i][1]
                        ret.append(t)
                        i+=1
                        break
                    else:
                        i+=1
                
                continue

            elif t[0]==-1 and intervals[i][0]>new[0]:
                t[0]=new[0]
                #print("B")
                while True and i <len(intervals):
                    if new[1]<intervals[i][0]:
                        t[1]=new[1]
                        ret.append(t)
                        break
                    elif new[1]<=intervals[i][1]:
                        t[1]=intervals[i][1]
                        ret.append(t)
                        i+=1
                        break
                    else:
                        i+=1
                continue

            else:
                ret.append(intervals[i])
            i+=1

        if t[0]==-1:
            ret.append(new)
        elif t[1]==-1:
            t[1]=new[1]
            ret.append(t)
        return ret