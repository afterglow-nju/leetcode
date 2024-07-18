class DetectSquares:
    
    def __init__(self):
        #self.row=defaultdict(list)
        self.col=defaultdict(list)
        self.num=defaultdict(lambda :defaultdict(int))

    def add(self, point: List[int]) -> None:
        #self.row[point[0]].append(point[1])
        self.col[point[1]].append(point[0])
        self.num[point[0]][point[1]]+=1

    def count(self, point: List[int]) -> int:
        x,y=point[0],point[1]
        col=self.col[y]
        ans=0
        for i in col:
            dis=x-i
            if dis>0:
                #if x-dis in self.col[y-dis] and x in self.col[y-dis]:
                ans+=self.num[x-dis][y-dis]*self.num[x][y-dis]
                #if x in self.col[y+dis] and x-dis in self.col[y+dis]:
                ans+=self.num[x][y+dis]*self.num[x-dis][y+dis]
            elif dis<0:
                dis=-dis
                #if x in self.col[y-dis] and x+dis in self.col[y-dis]:
                ans+=self.num[x][y-dis]*self.num[x+dis][y-dis]
                #if x in self.col[y+dis] and x+dis in self.col[y+dis]:
                ans+=self.num[x][y+dis]*self.num[x+dis][y+dis]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)