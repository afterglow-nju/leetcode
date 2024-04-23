class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            try:
                if i=='}' and stack[-1]=='{':
                    del stack[-1]
                elif i==')' and stack[-1]=='(':
                    del stack[-1]
                elif i==']' and stack[-1]=='[':
                    del stack[-1]
                else:
                    stack.append(i)
            except:
                stack.append(i)
        return len(stack)==0   
            
