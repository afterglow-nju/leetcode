class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        s=[]
        for i in expression:
            if i in [',','(']:
                continue
            if i in ['&','|' ,'!' ,'f','t']:
                s.append(i)
            elif i==')':
                has_true=False
                has_false=False
                while s[-1] not in ['&','|','!']:
                    tem=s.pop()
                    if tem=='t':
                        has_true=True
                    elif tem=='f':
                        has_false=True
                
                tem=s.pop()
                if tem=='&':
                    s.append('t' if not has_false else 'f')
                elif tem=='|':
                    s.append('t' if has_true else 'f')
                elif tem=='!':
                    s.append('t' if has_false else 'f')
                else:
                    assert(0)
            else:
                assert(0)     
        return False if s[-1]=='f' else True

        '''
        def parse_ng(expre):
            tem=expre[2:len(expre)-1]
            return True if tem[0]=='f' else False
        def parse_and(expre):
            tem=expre[2:len(expre)-1]
            i=0
            while i<len(tem):
                if i=='f':
                    return False
                elif i=='t':
                    i+=2
                elif i==',':
                    i+=1
                else:
                    assert(0)
            return True
        def parse_or(expre):
            tem=expre[2:len(expre)-1]
            i=0
            while i<len(tem):
                if i=='f':
                    i+=2
                    continue
                elif i=='t':
                    return True
                elif i==',':
                    i+=1
                else:
                    assert(0)
            return False

        stack=[]
        index=[]
        flag=True
        for i in range(len(expression)):
            if expression[i]!=')':
                stack.append(experssion[i])
                if expression[i]=='&' or expression[i]=='|' or expression[i]=='!':
                    index.append(len(stack)-1)
            else:
                if stack[index[-1]]=='&':
                    flag=self.parse_and(stack[index[-1]:len(stack)])
                elif stack[index[-1]]=='|':
                    flag=self.parse_or(stack[index[-1]:len(stack)])
                elif stack[index[-1]]=='!':
                    flag=self.parse_ng(stack[index[-1]:len(stack)])
                stack=stack[0:index[-1]]
                index.pop()
        '''