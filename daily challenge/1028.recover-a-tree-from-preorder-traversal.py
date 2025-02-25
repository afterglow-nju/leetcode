class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        for i in range(30, -1, -1):
            if S.find('-' * i) != 0:
                S = S.replace('-' * i, chr(i + 65))
        
        def helper(s, depth):
            tmp = s.split(chr(depth + 65))
            root = TreeNode(tmp[0])
            root.left = helper(tmp[1], depth+1) if len(tmp) > 1 else None
            root.right = helper(tmp[2], depth+1) if len(tmp) > 2 else None
            return root
        
        return helper(S, 1)