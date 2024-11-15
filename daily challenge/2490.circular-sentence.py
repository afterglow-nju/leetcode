class Solution:
    def isCircularSentence(self, s: str) -> bool:
        dic=s.split(' ')
        for i in range(len(dic)-1):
            if dic[i][-1]==dic[i+1][0]:
                continue
            else:
                return False
        return dic[0][0]==dic[-1][-1]    