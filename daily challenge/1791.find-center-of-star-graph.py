class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d=defaultdict(int)
        for i in edges:
            d[i[0]]+=1
            d[i[1]]+=1
            if d[i[0]]>1:
                return i[0]
            if d[i[1]]>1:
                return i[1]
        assert(o)