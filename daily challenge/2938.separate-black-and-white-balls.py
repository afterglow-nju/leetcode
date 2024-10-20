class Solution:
    def minimumSteps(self, s: str) -> int:
        ret=0
        one=[]
        for i in range(len(s)):
            if s[i]=='1':
                one.append(i)
        num=len(one)
        blank=[]
        for i in range(len(s)-num,len(s)):
            if s[i]=='0':
                blank.append(i)
        #print(one,blank)
        for i in range(len(blank)):
            ret+=blank[i]-one[i]
        return ret

        '''
        s='0'+s+'1'
        left,right=0,len(s)-1
        index=1
        ret=0
        while index<right:
            if s[index]=='0':
                index+=1
            else:
                if index==right:
                    break
                else:
                    #print(s,right)
                    right-=1
                    while s[right]=='1':
                        right-=1
                    #s[right]='1'
                    ret+=1
                    index+=1
        return ret
        '''