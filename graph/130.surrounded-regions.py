class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        con=set()
        def connect(i,j):
            if i<0 or j<0 or i>len(board)-1 or j>len(board[0])-1:
                return False
            if board[i][j]=='X':
                return True
            if i==0:
                if (i+1,j) not in con:
                    return False
            if j==0:
                if (i,j+1) not in con:
                    return False
            if i==len(board)-1:
                if (i-1,j) not in con:
                    return False
            if j==len(board[0])-1:
                if (i,j-1) not in con:
                    return False
            
            if (i,j) in con:
                return True
            else:
                con.add((i,j))
                if connect(i+1,j) and connect(i-1,j) and connect(i,j+1) and connect(i,j-1):
                    return True
                else:
                    con.clear()

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j]=='O':
                    connect(i,j)
                    for k in con:
                        board[k[0]][k[1]]='X'
                    con.clear()
        


        '''
        visit=[[True]*(len(board[0])) for _ in range(len(board))]
        def bfs(i,j,flag=True):
            
            if i<0 or j<0 or i>len(board)-1 or j>len(board[0])-1:
                return False
            print(i,j)
            if not visit[i][j]:
                #print(i,j)
                return True#board[i][j]=='X'
            print("!")
            
            if board[i][j]=='X':
                return True
            else:
                visit[i][j]=False
                if bfs(i+1,j) and bfs(i-1,j) and bfs(i,j-1) and bfs(i,j+1):
                    board[i][j]='X'
                    return True
                else:
                    #print(i,j)
                    board[i][j]='O'
                    return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j]=='O':
                    a=bfs(i,j)
                    print("?",i,j,a)
                visit[i][j]=False
                
        '''