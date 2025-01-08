class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        index=0
        for i in range(len(str1)):
            if index<len(str2):
                a,b=ord(str2[index]),ord(str1[i])
                if 0<=a-b<=1 or (a==ord('a') and b==ord('z')):
                    index+=1
            else:
                return True
        return index>=len(str2)
        