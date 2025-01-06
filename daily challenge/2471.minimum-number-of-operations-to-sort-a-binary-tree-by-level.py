# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ret=0

        q=[root]
        while q:
            tem=[]
            a=[]
            for node in q:
                #node=q.pop()
                a.append(node.val)
                if node.left:
                    #a.append(node.left.val)
                    tem.append(node.left)
                if node.right:
                    #a.append(node.right.val)
                    tem.append(node.right)
            q=tem
            #print(a,ret)
            n = len(a)
            a = sorted(range(n), key=lambda i: a[i])  # 离散化
            ret+=n
            vis = [False]*n
            for v in a:
                if vis[v]:
                    continue
                else:
                    while not vis[v]:
                        vis[v]=True
                        v=a[v]
                    ret-=1
        #https://www.cnblogs.com/lipu123/p/14728643.html
        #假设有m个环，完成任务总的交换次数 = 环1元素个数-1+环2元素个数-1+....+环m元素个数-1  = （环1元素个数+环2元素个数+.....+环m元素个数 = 数列元素总个数）- (1+1+....+1 = m)。
        #所以ret初始化为元素个数，然后while循环看有几个环
        return ret

            