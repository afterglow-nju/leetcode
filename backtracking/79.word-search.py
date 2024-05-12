class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        m,n=len(board)-1,len(board[0])-1
        def search(a,b,index):
            nonlocal m,n
            if index==len(word):
                return True
            if a<0 or a>m or b<0 or b>n:
                return False
            if board[a][b]==word[index]:
                t=board[a][b]
                board[a][b]=0
                
                index+=1
                ret= search(a+1,b,index) or \
                        search(a-1,b,index) or \
                        search(a,b+1,index) or \
                        search(a,b-1,index)
                board[a][b]=t
                return ret
       
        for i in range(m+1):
            for j in range(n+1):
                if search(i,j,0):
                    return True
        return False