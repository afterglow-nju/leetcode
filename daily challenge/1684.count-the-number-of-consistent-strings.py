class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        ret=0
        for i in words:
            tem=set(i)
            if tem.issubset(a):
                ret+=1
        return ret