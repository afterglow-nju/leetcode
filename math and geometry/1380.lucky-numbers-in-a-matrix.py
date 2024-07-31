class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #因为unique value, 所以唯一
        for i in range(len(matrix)):
            index=matrix[i].index(min(matrix[i]))
            value=matrix[i][index]
            flag=True
            for j in range(len(matrix)):
                if value>=matrix[j][index]:
                    continue
                else:
                    flag=False
                    break
            if flag:
                return [value]
        return []