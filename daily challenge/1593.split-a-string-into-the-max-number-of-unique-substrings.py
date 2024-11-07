class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(start,S):
            if start==len(s):
                return 0
            tem=0
            for i in range(start,len(s)):
                if s[start:i+1] not in S:
                    S.add(s[start:i+1])
                    tem=max(tem,1+dfs(i+1,S))
                    S.remove(s[start:i+1])
            return tem
        return dfs(0,set())