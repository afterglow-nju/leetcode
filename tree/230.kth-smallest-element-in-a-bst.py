# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        index=[0]
        ret=[None]
        def dfs(node):
            if not node:
                return
            if index[0]>k:
                return 
            dfs(node.left)
            index[0]+=1
            if index[0]==k:
                ret[0]=node.val
                return
            
            dfs(node.right)

        dfs(root)

        return ret[0]