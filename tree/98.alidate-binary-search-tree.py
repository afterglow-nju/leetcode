# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre=[float('-inf')]
        ret=[1]
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if pre[0]>=node.val:
                ret[0]=0
            pre[0]=node.val
            dfs(node.right)
        dfs(root)
        return bool(ret[0])


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ret=[]
        def valid(node):
            if not node:
                return None
            valid(node.left)
            ret.append(node.val)
            valid(node.right)
        valid(root)
        for i in range(0,len(ret)-1):
            if ret[i+1]<=ret[i]:
                return False
        return True