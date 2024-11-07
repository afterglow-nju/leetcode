# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q=[root]
        ret=[]
        while q:
            tem=[]
            s=0
            for i in q:
                s+=i.val
                if i.left:
                    tem.append(i.left)
                if i.right:
                    tem.append(i.right)
            ret.append(s)
            q=tem
        ret.sort(reverse=True)
        return -1 if k>len(ret) else ret[k-1]
                 