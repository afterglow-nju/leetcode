class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left,right=0,0
        ret=[]
        def gener(now,l,r):
            if l==n and r==n:
                ret.append(now)
                return
            if r<l:
                gener(now+')',l,r+1)
                if l<n:
                    gener(now+'(',l+1,r)
                
            if r==l:
                gener(now+'(',l+1,r)
        gener("",0,0)
        return ret