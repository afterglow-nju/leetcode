class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        mod=10**(n-1)
        visit=set()
        ans=[]
        def dfs(node):
            for i in range(k):
                edge=node*10+i
                if edge in visit:
                    continue
                else:
                    visit.add(edge)
                    nxt=edge%mod #因为每个节点代表是n-1位，通过取余第一位不要，要后面n-1位
                    dfs(nxt)
                    ans.append(str(i))
        dfs(0)
        return "".join(ans)+'0'*(n-1)