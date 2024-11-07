class Solution:
    def makeFancyString(self, s: str) -> str:
        ret=""
        prev=""
        tem=0
        for i in s:
            if prev==i:
                tem+=1
            else:
                prev=i
                tem=0
            if tem<2:
                ret+=i
        return ret