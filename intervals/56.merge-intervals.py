class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        ret=[]
        d=defaultdict(list)
        # 0=beg 1=end 重叠看beg
        for i in nums:
            if d[i[0]]==[]:
                d[i[0]]=[1,0]
            else:
                d[i[0]][0]+=1
            if d[i[1]]==[]:
                d[i[1]]=[0,1]
            else:
                d[i[1]][1]+=1
            
        d=dict(sorted(d.items(),key=lambda y: y[0]))
        a1,a2=-1,-1
        beg,end=0,0
        for i,j in d.items():
            beg+=j[0]
            end+=j[1]
            if j[1]>0:
                a2=i
            if a1==-1:
                a1=i

            if beg==end:
                ret.append([a1,a2])
                a1=-1
                a2=-1
        
        return ret