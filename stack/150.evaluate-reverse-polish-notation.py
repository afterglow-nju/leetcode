class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in ['+','-','*','/']:
                stack.append(int(i))
            else:
                try:
                    a=str(stack.pop())
                    b=str(stack.pop())
                    s=int(eval(b+i+a))
                    stack.append(s)
                except:
                    return i
        return stack[0]
                