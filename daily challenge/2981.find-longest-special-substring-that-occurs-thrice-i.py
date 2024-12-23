class Solution:
    def maximumLength(self, st: str) -> int:
        d=defaultdict(lambda:[])

        index=0
        for i in range(1,len(st)):
            if st[index]==st[i]:
                continue
            else:
                while index<i:
                    d[st[index]].append(i-1-index+1)
                    index+=1
        ret=-1
        while index<len(st):
            d[st[index]].append(len(st)-1-index+1)
            index+=1
        for i in d:
            #print(d[i])
            if len(d[i])>=3:
                d[i].sort(reverse=True)
                ret=max(ret,d[i][2])
        return ret
            