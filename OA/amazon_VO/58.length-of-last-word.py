class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ret=0
        index=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                continue
            else:
                index=i
                break
        ret=index
        while index>=0:
            if s[index]!=' ':
                index-=1
            else:
                break
        return ret-(index+1)+1