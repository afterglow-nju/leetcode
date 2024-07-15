# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d=defaultdict(int)
        p,c=set(),set()
        for i in descriptions:
            p.add(i[0])
            c.add(i[1])
            parent,child=d[i[0]],d[i[1]]
            if parent==0:
                parent=TreeNode(i[0])
            if child==0:
                child=TreeNode(i[1])
            if i[2]==1:
                parent.left=child
            else:
                parent.right=child
            d[i[0]]=parent
            d[i[1]]=child
            
        return d[(p-c).pop()]