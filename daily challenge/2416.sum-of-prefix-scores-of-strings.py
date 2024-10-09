class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class Trie:
            def __init__(self,root=False):
                self.child=dict()
                self.root=root
                self.count=0
            def insert(self, word: str) -> None:   
                nxt=self
                for i in word:
                    if not nxt.child.get(i,None):
                        nxt.child[i]=Trie()
                    nxt.child[i].count+=1
                    nxt=nxt.child[i]
                nxt.root=True
            def search(self, word: str) -> bool:
                nxt=self
                for i in word:
                    if not nxt.child.get(i,None):
                        return False
                    else:
                        nxt=nxt.child[i]
                return nxt.root
            def startsWith(self, prefix: str) -> bool:
                nxt=self
                tem=0
                for i in prefix:
                    if not nxt.child.get(i,None):
                        return 0
                    else:
                        nxt=nxt.child[i]
                        tem+=nxt.count

                return tem
            def find(self):
                depth=0
                cur=self
                while len(cur.child)==1:
                    depth+=1
                    cur=list(cur.child.values())[0]
                return depth
        T=Trie()
        for i in words:
            T.insert(i)
        ret=[]
        for i in words:
            tem=T.startsWith(i)
            ret.append(tem)
        return ret
        '''
        d=defaultdict(int)
        for i in words:
            for j in range(len(i)):
                d[i[0:j+1]]+=1
        ret=[]
        for i in words:
            tem=0
            for j in range(len(i)):
                tem+=d[i[0:j+1]]
            ret.append(tem)
        return ret
        '''