class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        node=[0]*n
        for i in roads:
            node[i[0]]+=1
            node[i[1]]+=1
        node.sort()
        ret=0
        for i in range(1,n+1):
            ret+=node[i-1]*i
        return ret