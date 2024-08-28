class Solution:
    def fractionAddition(self, expression: str) -> str:
        #print(expression,expression[0])
        if expression[0]=='-':
            tem1=1
            while expression[tem1]!='/':
                tem1+=1
            tem2=tem1+1
            while tem2<len(expression) and expression[tem2]!='+' and expression[tem2]!='-' :
                tem2+=1
            index=tem2
            upp=-int(expression[1:tem1])
            bot=int(expression[tem1+1:tem2])
        else:
            tem1=0
            while expression[tem1]!='/':
                tem1+=1
            tem2=tem1+1
            while tem2<len(expression) and expression[tem2]!='+' and expression[tem2]!='-' :
                tem2+=1
            index=tem2
            upp=int(expression[0:tem1])
            bot=int(expression[tem1+1:tem2])
        print(upp,bot)
        #print("!",index)
        while index<len(expression):
            if expression[index]=='+':
                flag=1
            else:
                flag=-1
            index+=1
            #print(index)
            tem1=index
            while expression[tem1]!='/':
                tem1+=1
            tem2=tem1+1
            while tem2<len(expression) and expression[tem2]!='+' and expression[tem2]!='-' :
                tem2+=1
            
            #print("!",tem1,tem2,index)
            print(expression[tem1+1:tem2],expression[index:tem1])
            upp=upp*int(expression[tem1+1:tem2])+flag*int(expression[index:tem1])*bot
            bot=bot*int(expression[tem1+1:tem2])
            print(upp,bot)
            index=tem2
        gcd=math.gcd(upp,bot)
        #print(gcd)
        upp//=gcd
        bot//=gcd
        return str(upp)+'/'+str(bot)