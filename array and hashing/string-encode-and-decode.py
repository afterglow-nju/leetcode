#其实是错误的，应该用自身的长度作为分隔符
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        ret=''
        for i in strs:
            ret+=i+'1#'
        return ret
    def decode(self, s: str) -> List[str]:
        ret=s.split('1#')
        ret.pop()
        return ret