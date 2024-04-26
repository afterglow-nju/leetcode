class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])-1
        left=0
        right=m-1
        
        while left<=right:
            mid=(right-left)//2+left
            print(mid)
            if target<matrix[mid][0]:
                right=mid-1
            elif target>matrix[mid][n]:
                left=mid+1
            else:
                break
        l=0
        r=n
        while l<=r:
            m=(r-l)//2+l
            t=matrix[mid][m]
            if t<target:
                l=m+1
            elif t>target:
                r=m-1
            else:
                return True
        return False
