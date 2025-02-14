class Solution:
    def merge(self, intv: List[List[int]]) -> List[List[int]]:
        intv.sort(key=lambda x:x[0])
        ret=[]
        i=1
        prev=intv[0]
        while i<len(intv):
            
            if prev[1]<intv[i][0]:
                ret.append(prev)
                prev=intv[i]
            else:
                #intv[i][0]<=prev[1]<=intv[i][1]:
                prev=[prev[0],max(prev[1],intv[i][1])]
            i+=1
        if not ret or ret[-1]!=prev:
            ret.append(prev)
        return ret
            