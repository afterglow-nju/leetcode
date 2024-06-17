class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        s=[i**2 for i in range(65536)]
        d=defaultdict(int)
        for i in s:
            d[i]=1
        for i in s:
            if d[c-i]==1:
                return True
        return False
        '''
        i=0
        j=int(c**0.5)+1
        while i<=j:
            a=i**2+j**2
            if a>c:
                j-=1
            elif a<c:
                i+=1
            else:
                return True
        return False