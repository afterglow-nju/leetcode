class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def count(mid):
            pre=position[0]
            c=1
            for i in range(len(position)):
                if position[i]-pre>=mid:
                    pre=position[i]
                    c+=1
            return c>=m

        left,right=0,position[-1]
        while left<=right:
            mid=(right-left)//2+left
            
            if count(mid):
                left=mid+1
            else:
                right=mid-1
            #print(left,right)
        return right

