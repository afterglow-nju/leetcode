class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        '''KMP模板'''
        def prefix_function(s):     
            n = len(s)
            pi = [0] * n

            j = 0
            for i in range(1, n):
                while j>0 and s[i] != s[j]:     # 当前位置s[i]与s[j]不等
                    j = pi[j-1]                 # j指向之前位置，s[i]与s[j]继续比较

                if s[i] == s[j]:                # s[i]与s[j]相等，j+1，指向后一位
                    j += 1
                
                pi[i] = j
            return pi
        

        '''主程序'''
        pi = prefix_function(s+'#'+s[::-1])     # s+'#'+s[n-1,...,0]的前缀函数
        if pi[-1] == len(s):                    # 前缀函数的最后一位即为s的最长回文前缀的长度
            return s
        else:
            return s[pi[-1]:][::-1] + s
