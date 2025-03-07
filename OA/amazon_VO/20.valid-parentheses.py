class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {')':'(', ']':'[', '}':'{'}
        stack = []

        for i in s:
            if i in mapper:
                if stack and stack[-1]==mapper[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0

            