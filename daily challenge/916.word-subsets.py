class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ret=[]
        v=defaultdict(int)
        for i in words2:
            tem=Counter(i)
            for key,value in tem.items():
                if value>v[key]:
                    v[key]=value

        for i in words1:
            t=Counter(i)
            flag=True
            for key,value in v.items():
                if t[key]>=value:
                    continue
                else:
                    flag=False
                    break
            if flag:
                ret.append(i)
        return ret