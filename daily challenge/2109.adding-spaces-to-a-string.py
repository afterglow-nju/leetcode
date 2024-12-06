class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ret=""
        index=0
        for i in range(len(s)):
            if index<len(spaces) and i==spaces[index]:
                ret+=" "
                index+=1
            ret+=s[i]
        return ret