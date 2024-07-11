class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ret=0
        for i in logs:
            if i=='./':
                continue
            elif i=='../':
                ret=max(ret-1,0)
            else:
                ret+=1
        return max(0,ret)