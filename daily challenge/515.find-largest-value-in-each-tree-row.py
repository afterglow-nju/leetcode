# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ret=[]
        if not root:
            return ret
        q=[root]
        tem=[root.val]
        while q:
            ret.append(max(tem))
            tem=[]
            newq=[]
            while q:
                t=q.pop()
                if t.left:
                    newq.append(t.left)
                    tem.append(t.left.val)
                if t.right:
                    newq.append(t.right)
                    tem.append(t.right.val)
            q=newq
        return ret
