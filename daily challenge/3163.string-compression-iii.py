class Solution:
    def compressedString(self, word: str) -> str:
        ret=""
        index=0
        prev=""
        while index<len(word):
            if prev=="":
                prev=word[index]
                index+=1
            else:
                cnt=1
                while index<len(word) and prev==word[index]:
                    cnt+=1
                    index+=1
                    if cnt>=9:
                        break
                ret+=str(cnt)+prev
                prev=""
                #print(ret,index)
                if index<len(word):
                    prev=word[index]

                index+=1
                
                #print(index,prev)
        if prev!="":
            ret+='1'+word[-1]
        return ret
            