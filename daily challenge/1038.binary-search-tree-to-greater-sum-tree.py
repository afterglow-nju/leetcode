# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        v=[0]
        def dfs(node): # inorder
            
            if not node:
                return 
            
            dfs(node.right)
            v[0]+=node.val
            node.val=v[0]
            dfs(node.left)
            
        
        dfs(root)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        v=[0]
        def dfs(node,value): # inorder
            
            if not node:
                return False
            
            dfs(node.right,value)
            v[0]+=node.val
            node.val=v[0]
            dfs(node.left,value)
            
        
        dfs(root,0)
        return root