class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        set1=(s1.split(' '))
        set2=(s2.split(' '))
        d1=defaultdict(int)
        #d2=defaultdict(int)
        for i in set1:
            d1[i]+=1
        for i in set2:
            d1[i]+=1
        #tem1,tem2=set(),set()
        
        ret=[]
        for i in d1:
            if d1[i]==1:
                ret.append(i)
        return ret

        '''
        for i in set1:
            if d1[i]==1 and d2[i]==0:
                tem1.add(i)
        for i in set2:
            if d2[i]==1 and d1[i]==0:
                tem2.add(i)
        #print(tem1,tem2)
        
        return list(tem1-tem2)+list(tem2-tem1)
        '''