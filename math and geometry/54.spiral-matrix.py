class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret=[]
        low,high=0,len(matrix)-1
        left,right=0,len(matrix[0])-1
        while low<=high and left<=right:
            for i in range(left,right+1):
                ret.append(matrix[low][i])
            for i in range(low+1,high+1):
                ret.append(matrix[i][right])

            if  (low==high) or left==right:
                break 
            for i in range(right-1,left-1,-1):
                ret.append(matrix[high][i])
            for i in range(high-1,low,-1):
                ret.append(matrix[i][left])
            low+=1
            high-=1
            left+=1
            right-=1
        return ret