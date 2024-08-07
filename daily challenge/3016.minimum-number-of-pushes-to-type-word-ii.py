class Solution:
    def minimumPushes(self, word: str) -> int:
        #读题读了好久
        c=Counter(word)
        c=sorted(c.items(),reverse=True, key=lambda x:x[1])
        index,count,ret=1,8,0
        for i in c:
            if count>0:
                count-=1
                ret+=(i[1]*index)
            else:
                count=7
                index+=1
                ret+=(i[1]*index)
        return ret
