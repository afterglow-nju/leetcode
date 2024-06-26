# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        a=[]
        def dfs(node):
            if not node:
                return
            if node.left:
                dfs(node.left)
            a.append(node)
            if node.right:
                dfs(node.right)
                
        dfs(root)
        n=len(a)
        def divide(left,right):
            if right-left<0:
                return None
            mid=(right-left)//2+left
            t=a[mid]
            #print(left,mid,right)
            t.left=divide(left,mid-1)
            t.right=divide(mid+1,right)
            #print(t.val)
            return t
        t=divide(0,n-1)
        return t