class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        while part in s:
            index=s.find(part)
            s=s[:index]+s[index+len(part):]
        return s
        '''
        stack=[]
        n=len(part)
        for i in s:
            stack.append(i)
            #print(stack)
            while len(stack)>=n:
                #print(stack[-n:])
                if "".join(stack[-n:])==part:
                    stack=stack[:-n]
                else:
                    break
        return "".join(stack)
        '''