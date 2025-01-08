class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ret=0
        n=len(words)
        for i in range(n):
            w=words[i]
            for j in range(i+1,n):
                if words[j].find(w)==0 and words[j].rfind(w)+len(w)==len(words[j]):
                    ret+=1
        return ret