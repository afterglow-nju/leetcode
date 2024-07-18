class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        level=0
        while level<=n-1:
            #print(n-level-1)
            for i in range(n-level-1):
                i1,j1=level//2,level//2+i
                i2,j2=level//2+i,n-1-level//2
                i3,j3=n-1-level//2,n-1-level//2-i
                i4,j4=n-1-level//2-i,level//2
                #print(i1,j1,i2,j2,i3,j3,i4,j4)

                a,b,c,d=matrix[i1][j1],matrix[i2][j2],matrix[i3][j3],matrix[i4][j4]
                matrix[i1][j1],matrix[i2][j2],matrix[i3][j3],matrix[i4][j4]=d,a,b,c
            level+=2