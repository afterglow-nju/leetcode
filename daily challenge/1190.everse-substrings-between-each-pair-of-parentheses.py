class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                left=stack.pop()
                s=s[:left]+s[left:i+1][::-1]+s[i+1:]
                #print(s)
        #print(s)
        t=""
        for i in s:
            if i!='(' and i!=')':
                t+=i
        return t