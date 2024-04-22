# not elegant
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1,dic2=dict(),dict()
        for i in s:
            dic1[i]=dic1.get(i,0)+1
        for i in t:
            dic2[i]=dic2.get(i,0)+1
        if len(dic1)==len(dic2):
            for i in dic1.keys():
                if dic1[i]==dic2.get(i,None):
                    continue
                return False
            return True
        return False