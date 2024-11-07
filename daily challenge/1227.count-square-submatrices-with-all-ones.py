class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def Sum(x,y,s):
            ret=0
            for i in range(x,x+s):
                ret+=sum(matrix[i][y:y+s])
            return ret==s**2
        
        ret=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(1,1+min(len(matrix)-i,len(matrix[0])-j)):
#                    print(i,j,k)
                    if Sum(i,j,k):
                        ret+=1
                    else:
                        break
        return ret