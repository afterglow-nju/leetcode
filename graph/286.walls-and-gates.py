class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        from typing import (
    List,
)

        q=deque()
        d=[[-1,0],[1,0],[0,1],[0,-1]]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j]==0:
                    q.append((i,j))
        while q:
            n=q.popleft()
            for i in d:
                t1,t2=n[0]+i[0],n[1]+i[1]
                if 0<=t1<len(rooms) and 0<=t2<len(rooms[0]) and rooms[t1][t2]!=-1:
                    if rooms[t1][t2]>rooms[n[0]][n[1]]+1:
                        rooms[t1][t2]=rooms[n[0]][n[1]]+1
                        q.append((t1,t2))
        

