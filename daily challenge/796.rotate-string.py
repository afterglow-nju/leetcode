class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        return len(s)==len(goal) and goal in s+s
        
        if len(s)!=len(goal):
            return False
        n=len(s)
        for i in range(n):#n-i=x-1-0+1
            if s[i:n]==goal[:n-i] and s[0:i]==goal[n-i:n]: 
                return True
        return False
        '''
        tem=""
        index=0
        for i in range(n):
            if s[i]!=goal[index]:
                if index!=0:
                    return False
                tem+=s[i]
            else:
                index+=1
        #print(tem,index,goal[index+1:n])
        return  tem==goal[index:n]
        '''