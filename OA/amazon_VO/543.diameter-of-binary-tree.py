# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret=[0]
        def dfs(node):
            if not node:
                return 0
            left,right=0,0
            if node.left:
                left=dfs(node.left)+1
            if node.right:
                right=dfs(node.right)+1
            ret[0]=max(ret[0],left+right)
            #print(node.val,left,right)
            return max(left,right)
        dfs(root)
        return ret[0]
