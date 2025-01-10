class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ret=0
        for i in words:
            if i.find(pref)==0:
                ret+=1
        return ret