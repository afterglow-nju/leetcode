# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        ret=[]
        q=deque()
        q.append(root)

        while q:
            tem=[]
            size=len(q)
            for i in range(size):
                t=q.popleft()
                tem.append(t.val)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)

            ret.append(tem)
        return ret


