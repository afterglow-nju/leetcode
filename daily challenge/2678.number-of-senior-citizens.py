class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for i in details:
            if i[11]>'6' or (i[11]=='6' and i[12]!='0'):
                ans+=1
        return ans