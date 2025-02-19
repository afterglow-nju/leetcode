class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ret=[]
        s=[]
        num=1
        for i in pattern:
            if i=='I':
                ret.append(num)
                while s:
                    t=s.pop()
                    ret.append(t)
                
            else:
                s.append(num)
            num+=1
        ret.append(num)
        while s:
            ret.append(s.pop())
        
        ret=[str(i) for i in ret]
        return "".join(ret)