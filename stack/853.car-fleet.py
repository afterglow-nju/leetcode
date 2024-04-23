class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        ret=0
        position,speed=zip(*sorted(list(zip(position,speed)),key=lambda x:x[0],reverse=True))
        for i,n in enumerate(position):
            #print(stack)
            if not stack:
                stack.append(i)
                p=n
                s=speed[i]
            else:
                if (target-n)/speed[i] <= (target-p)/s:
                    stack.append(i)
                else:
                    ret+=1
                    stack.clear()
                    #print("here")
                    stack.append(i)
                    p=n
                    s=speed[i]
        if stack:
            ret+=1
        return ret