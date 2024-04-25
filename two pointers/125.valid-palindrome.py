class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(filter(str.isalnum,s.lower()))
        print(s)
        n=len(s)
        left=0
        right=n-1
        for i in range(n//2):
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True