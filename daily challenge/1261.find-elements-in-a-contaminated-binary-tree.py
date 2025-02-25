# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.s=set()
        q=deque()
        q.append(root)
        self.s.add(0)
        root.val=0

        while q:
            t=q.popleft()
            if t.left:
                t.left.val=t.val*2+1
                q.append(t.left)
                self.s.add(t.left.val)
            if t.right:
                t.right.val=t.val*2+2
                q.append(t.right)
                self.s.add(t.right.val)


    def find(self, target: int) -> bool:
        if target in self.s:
            return True
        else:
            return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)