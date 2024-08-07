class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        d = {0: "Zero",
        1: "One ",
        2: "Two ",
        3: "Three ",
        4: "Four ",
        5: "Five ",
        6: "Six ",
        7: "Seven ",
        8: "Eight ",
        9: "Nine ",
        10: "Ten ",
        11: "Eleven ",
        12: "Twelve ",
        13: "Thirteen ",
        14: "Fourteen ",
        15: "Fifteen ",
        16: "Sixteen ",
        17: "Seventeen ",
        18: "Eighteen ",
        19: "Nineteen ",
        20: "Twenty ",
        30: "Thirty ",
        40: "Forty ",
        50: "Fifty ",
        60: "Sixty ",
        70: "Seventy ",
        80: "Eighty ",
        90: "Ninety ",
        100: "Hundred ",
        1000: "Thousand ",
        1000000: "Million ",
        1000000000: "Billion "
        }
        num = [int(digit) for digit in str(num)]
        
        num=num[::-1]
        ret=""
        right,left=2,0
        flag=False
        while True:
            if right<len(num):
                if num[right]*100+num[right-1]*10+num[right-2]==0:
                    right+=3
                    left+=3
                    flag=True
                    continue
                    
                if flag:
                    if right>=9:
                        ret=d[1000000000]+ret
                    elif right>=6:
                        ret=d[1000000]+ret
                    else:
                        ret=d[1000]+ret
                if num[right]*100+num[right-1]*10+num[right-2] in d:
                    print("here")
                    if num[right]!=0:
                        ret=d[num[right]]+d[num[right]*100+num[right-1]*10+num[right-2]]+ret
                    else:
                        ret=d[num[right]*100+num[right-1]*10+num[right-2]]+ret
                else:
                    if num[right-1]*10+num[right-2] in d:
                        if num[right]!=0:
                            ret=d[num[right]]+d[100]+d[num[right-1]*10+num[right-2]]+ret
                        else:
                            ret=d[num[right-1]*10+num[right-2]]+ret
                    else:
                        if num[right]!=0:
                            ret=d[num[right]]+d[100]+d[num[right-1]*10]+d[num[right-2]]+ret
                        else:
                            ret=d[num[right-1]*10]+d[num[right-2]]+ret
                right+=3
                left+=3
                flag=True
            else:
                print(len(num),left,right)
                if len(num)-left==1:
                    if right>=9:
                        ret=d[num[left]]+d[1000000000]+ret
                    elif right >=6:
                        ret=d[num[left]]+d[1000000]+ret
                    else:
                        if left!=0:
                            ret=d[num[left]]+d[1000]+ret
                        else:
                            ret=d[num[left]]

                elif len(num)-left==2:
                    tem=""
                    if num[left+1]==1:
                        tem=d[num[left+1]*10+num[left]]
                    else:
                        if num[left]!=0:
                            tem=d[num[left+1]*10]+d[num[left]]
                        else:
                            tem=d[num[left+1]*10]

                    if right>=9:
                        ret=tem+d[1000000000]+ret
                    elif right >=6:
                        ret=tem+d[1000000]+ret
                    else:
                        if left!=0:
                            ret=tem+d[1000]+ret
                        else:
                            ret=tem
                break
        
        #print(ret)
        ret=ret.replace("Zero", "")

        return ret[:-1]