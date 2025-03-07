class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        ret=[[1],[1,1]]
        
        for i in range(2,numRows):
            #print(ret)
            t=[1]
            h=ret[-1]
            for j in range(len(h)-1):
                t.append(h[j]+h[j+1])
            t.append(1)
            ret.append(t)
        return ret

