
class Trie:

    def __init__(self,root=False):
        self.child=dict()
        self.root=root

    def insert(self, word: str) -> None:
        
        nxt=self
        for i in word:
            if not nxt.child.get(i,None):
                nxt.child[i]=Trie(False)
            #print(word[i],nxt.child.keys())
            nxt=nxt.child[i]
        #print(nxt.child.keys())
        nxt.root=True

    def search(self, word: str) -> bool:
        nxt=self
        #print(word)
        for i in word:
            #print(nxt.child.keys)
            if not nxt.child.get(i,None):
                return False
            else:
                nxt=nxt.child[i]
        #print(nxt.root,word)
        return nxt.root
        '''
        if nxt.root:
            nxt.root=False
            return True
        else:
            return False
        '''


    def startsWith(self, prefix: str) -> bool:
        nxt=self
        for i in prefix:
            #print(nxt.child.keys)
            if not nxt.child.get(i,None):
                return False
            else:
                nxt=nxt.child[i]
                
        return True

'''
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Trie:
    def __init__(self):
        self.mp = {}

    def insert(self, word: str) -> None:
        curr = self.mp
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['#'] = True

    def search(self, word: str) -> bool:
        curr = self.mp
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        if '#' in curr:
            del curr['#']
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.mp
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d=Trie()
        for i in words:
            d.insert(i)
        ret=[]
        #valid=[[True]*len(board[0]) for _ in range(len(board))]
        ROW=len(board)
        COL=len(board[0])
        def bfs(i,j,s,node):
            shift=[(1,0),(0,1),(-1,0),(0,-1)]
            if board[i][j]!=0:
                if board[i][j] in node.child:
                    t=s+board[i][j]
                    #if t in words:
                    #    ret.append(t)
                    #    words.remove(t)
                    r=board[i][j]
                    board[i][j]=0
                    node=node.child[r]
                    if node.root:
                        ret.append(t)
                        node.root=False

                    for k in shift:
                        if 0<=i+k[0]<ROW and 0<=j+k[1]<COL:
                            bfs(i+k[0],j+k[1],t,node)
                    board[i][j]=r
                else:
                    return 
            else:
                return 

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                    #print(i,j)
                    bfs(i,j,"",d)
                    #valid=[[True]*len(board[0]) for _ in range(len(board))]
                    
        return ret
