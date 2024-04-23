class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(s,left,right): #s: current string i: current bracket
            ret=[]
            if right==n:
                return [s]
            if left<n:
                ret+=dfs(s+'(',left+1,right)
            if left>right and right<n:
                ret+=dfs(s+')',left,right+1)
            return ret
            
        return dfs("",0,0)