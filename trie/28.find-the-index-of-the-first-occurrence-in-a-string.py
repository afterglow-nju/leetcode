#KMP
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        
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
        ret=kmp.KMP(haystack,needle)
        return ret[0] if ret else -1
       #https://gist.github.com/m00nlight/daa6786cc503fde12a77