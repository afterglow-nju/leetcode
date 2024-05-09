# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ret=0
        def depth(node,d):
            if not node :
                return d
            left=node.left
            right=node.right
            t1=depth(left,d+1)
            t2=depth(right,d+1)
            return max(t1,t2)
        return depth(root,0)