class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        ret=[]
        for i in arr:
            if i%2==0:
                ret=[]
            else:
                ret.append(1)
                if len(ret)==3:
                    return True
        return False