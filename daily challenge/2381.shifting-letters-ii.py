class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        c2i = {c: i for i, c in enumerate(ascii_lowercase)}
        n = len(s)
        diff = [0] * (n + 1)
        for st,e,d in shifts:
            diff[st]+=d*2-1
            diff[e+1]-=d*2-1
        ret=""
        shift=0
        for i in range(n):
            shift+=diff[i]
            #print(i,shift)
            #print(ord('a')+(ord(s[i])-ord('a')+shift)%26)
            ret+=chr(ord('a')+(ord(s[i])-ord('a')+shift)%26)
        return ret