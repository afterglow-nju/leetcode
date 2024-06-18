class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c=False,False,False
        for i in triplets:
            if i[0]<=target[0] and i[1]<=target[1] and i[2]<=target[2]:
                if not a and i[0]==target[0]:
                    a=True
                if not b and i[1]==target[1]:
                    b=True
                if not c and i[2]==target[2]:
                    c=True
            if a and b and c:
                return True

        return a and b and c
