class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ret=[]
        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def back(ans,index):
            if index==len(digits):
                ret.append("".join(ans))
                return
            for j in d[digits[index]]:
                ans.append(j)
                back(ans,index+1)
                ans.pop()
        if not digits:
            return ret
        back([],0)
        return ret
            