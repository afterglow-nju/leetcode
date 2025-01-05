class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        b=[0]*n
        pre=[0]*n
        for i,x in enumerate(words):
            if x[0] in ['a','e','i','o','u'] and x[-1] in ['a','e','i','o','u']:
                b[i]=1
            pre[i]=pre[i-1]+b[i]
        ret=[]
        for i in queries:
            if i[0]>0:
                ret.append(pre[i[1]]-pre[i[0]-1])
            else:
                ret.append(pre[i[1]])
        return ret