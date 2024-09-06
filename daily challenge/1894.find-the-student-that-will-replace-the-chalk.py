class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        index=0
        n=len(chalk)
        s=sum(chalk)
        k%=s
        while True:
            #print(index)
            if chalk[index]<=k:
                k-=chalk[index]
            else:
                return index
                break
            index=(index+1)%(n)