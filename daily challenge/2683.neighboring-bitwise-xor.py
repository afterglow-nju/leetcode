class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        ret=0
        for i in derived:
            ret^=i
        return ret==0