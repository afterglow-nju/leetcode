class Solution:
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def count_differences(word1, word2):
            differences = sum(1 for a, b in zip(word1, word2) if a != b)
            return differences
        g=defaultdict(list)

        pattern=defaultdict(set)

        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                after=wordList[i][:j]+'*'+wordList[i][j+1:]
                pattern[after].add(i)


        for i in range(len(wordList)):
            s=set()
            for j in range(len(wordList[i])):
                after=wordList[i][:j]+'*'+wordList[i][j+1:]
                s|=pattern[after]
            g[i]=list(s)

        
        beg=[]
        from collections import deque
        q = deque()
        visit=[False]*len(wordList)
        ret=[0]

        for i in range(len(wordList)):
            if count_differences(wordList[i],beginWord)==1:
                q.append((i,1))
                visit[i]=True
                beg.append(i)

        while q:
            t=q.popleft()
            if wordList[t[0]]==endWord:
                return t[1]+1
            for i in g[t[0]]:
                if not visit[i]:
                    visit[i]=True
                    q.append((i,t[1]+1))
        return 0
        #assert(0)