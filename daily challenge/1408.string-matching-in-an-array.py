class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        class KMP:
            def partial(self,pattern):
                ret=[0]
                for i in range(1,len(pattern)):
                    j=ret[i-1]
                    while j>0 and pattern[i]!=pattern[j]:
                        j=ret[j-1]
                    ret.append(j+1 if pattern[i]==pattern[j] else j)
                return ret
            
            
            def KMP(self,t,p):
                partial,ret,j=self.partial(p),[],0
                for i in range(len(t)):
                    while j>0 and t[i]!=p[j]:
                        j=partial[j-1]
                    if t[i]==p[j]:
                        j+=1
                    if j==len(p):
                        ret.append(i-(j-1))
                        j=partial[j-1]
                return ret

        kmp=KMP()
        ret=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j:
                    continue
                tem=kmp.KMP(words[j],words[i])
                if len(tem)>0:
                    ret.append(words[i])
                    break
        return ret