class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:  # 空节点
            return None
        if len(preorder) == 1:  # 叶子节点
            return TreeNode(preorder[0])
        left_size = postorder.index(preorder[1]) + 1  # 左子树的大小
        left = self.constructFromPrePost(preorder[1: 1 + left_size], postorder[:left_size])
        right = self.constructFromPrePost(preorder[1 + left_size:], postorder[left_size: -1])
        return TreeNode(preorder[0], left, right)
