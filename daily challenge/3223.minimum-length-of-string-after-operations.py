class Solution:
    def minimumLength(self, s: str) -> int:
        c=Counter(s)
        ret=0
        for key,value in c.items():
            while value>=3:
                value-=2*(value//3)
           # print(key,value)
            ret+=value
        return ret