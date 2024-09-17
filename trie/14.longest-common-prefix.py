class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        class Trie:
            def __init__(self,root=False):
                self.child=dict()
                self.root=root
            def insert(self, word: str) -> None:   
                nxt=self
                for i in word:
                    if not nxt.child.get(i,None):
                        nxt.child[i]=Trie()
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
                for i in prefix:
                    if not nxt.child.get(i,None):
                        return False
                    else:
                        nxt=nxt.child[i]
                return True
            def find(self):
                depth=0
                cur=self
                while len(cur.child)==1:
                    depth+=1
                    cur=list(cur.child.values())[0]
                return depth
        trie=Trie()
        for i in strs:
            trie.insert(i)
        strs.sort()
        ret=trie.find()
        return strs[0][:min(len(strs[0]),ret)] if ret!=0 else ""
