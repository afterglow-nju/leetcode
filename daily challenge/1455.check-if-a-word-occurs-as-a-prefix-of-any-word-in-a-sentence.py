class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        s=sentence.split(' ')
        n=len(searchWord)
        for i,x in enumerate(s):
            if len(x)>=n and x[:n]==searchWord:
                return i+1
        return -1