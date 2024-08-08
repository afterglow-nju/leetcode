class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        r,c=rStart,cStart
        ret=[]
        d,td=1,1

        def clock(dirc,r,c,d):
            C,R=0,0
            Ret=[]
            if dirc=='right':
                C=1
            elif dirc=='down':
                R=1
            elif dirc=='left':
                C=-1
            else:
                R=-1
            Ret=[r+d*R,c+d*C]
            while d>0:
                c+=C
                r+=R
                if 0<=r<rows and 0<=c<cols:
                    ret.append([r,c])
                d-=1
            return Ret 
        tem=[r,c]
        ret.append(tem)
        while len(ret)<rows*cols:
            tem=clock('right',tem[0],tem[1],d)
            tem=clock('down',tem[0],tem[1],d)
            tem=clock('left',tem[0],tem[1],d+1)
            tem=clock('on',tem[0],tem[1],d+1)
            #print(len(ret),ret)
            d+=2
        return ret
            
            
