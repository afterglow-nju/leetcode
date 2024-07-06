class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        a=(time-1)//(n-1)
        print(a)
        if a%2==0:
            return time-a*(n-1)+1
        else:
            return n-(time-a*(n-1))