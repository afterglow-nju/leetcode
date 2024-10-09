class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        ret=[]
        op=['+','-','*']
        
        def calcu(expression):
            if expression=='':
                return []
            ans=[]
            for i in range(len(expression)):
                if expression[i] in op:

                    left=calcu(expression[:i])
                    right=calcu(expression[i+1:])
                    for j in left:
                        for k in right:
                            if expression[i]=='+':
                                ans.append(j+k)
                            elif expression[i]=='-':
                                ans.append(j-k)
                            else:
                                ans.append(j*k)
            if not ans:
                ans.append(int(expression))
            return ans 

        ret=calcu(expression)
        return ret
