class Solution:
    def maximumGain(self, string: str, x: int, y: int) -> int:
        s=[]
        target='ab' if x>y else 'ba'
        Max=max(x,y)
        Min=min(x,y)
        ret=0
        flag=False
        for i in string:
            if i==target[1] and len(s)>=1 and s[-1]==target[0]:
                s.pop()
                ret+=Max
            else:
                s.append(i)
        

        string="".join(s)
        s=[]
        for i in string:
            if i==target[0] and len(s)>=1 and s[-1]==target[1]:
                s.pop()
                ret+=Min
            else:
                s.append(i)
        return ret