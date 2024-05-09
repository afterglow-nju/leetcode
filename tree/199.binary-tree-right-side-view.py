# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret=[]
        if not root:
            return ret
        from collections import deque
        q=deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                t=q.popleft()
                if i==0:
                    ret.append(t.val)

                if t.right:
                    q.append(t.right)
                if t.left:
                    q.append(t.left)
                

        return ret