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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)