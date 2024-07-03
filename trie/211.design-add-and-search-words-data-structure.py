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

    def search(self, index,word: str,a=None) -> bool:
        if not a:
            nxt=self
        else:
            nxt=a
        for i in range(index,len(word)):
            if word[i] == '.':
                for j in nxt.child.keys():
                    if self.search(i+1,word,nxt.child[j]):
                        return True
                else:
                    return False
            if not nxt.child.get(word[i],None):
                return False
            else:
                nxt=nxt.child[word[i]]
        
        return nxt.root



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class WordDictionary:

    def __init__(self,root=False):
        self.child=dict()
        self.root=root

    def addWord(self, word: str) -> None:
        nxt=self
        for i in word:
            if not nxt.child.get(i,None):
                nxt.child[i]=Trie()
            nxt=nxt.child[i]
        nxt.root=True

    def search(self,word: str,index=0,a=None) -> bool:
        if not a:
            nxt=self
        else:
            nxt=a
        for i in range(index,len(word)):
            if word[i] == '.':
                for j in nxt.child.keys():
                    if self.search(word,i+1,nxt.child[j]):
                        return True
                else:
                    return False
            if not nxt.child.get(word[i],None):
                return False
            else:
                nxt=nxt.child[word[i]]
        
        return nxt.root


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)