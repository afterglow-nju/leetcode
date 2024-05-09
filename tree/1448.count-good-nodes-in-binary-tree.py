# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret=[0]

        def good(node,m):
            if not node:
                return
            if node.val>=m:
                m=node.val
                ret[0]+=1
            good(node.left,m)
            good(node.right,m)
        good(root,float('-inf'))
        return ret[0]