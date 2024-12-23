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
        
        return ret

            