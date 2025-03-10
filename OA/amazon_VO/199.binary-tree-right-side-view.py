# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level=set()
        ret=[]
        def dfs(n,d):
            if not n:
                return 
            if d not in level:
                level.add(d)
                ret.append(n.val)
            dfs(n.right,d+1)
            dfs(n.left,d+1)
        dfs(root,0)
        return ret