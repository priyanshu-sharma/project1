class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output = []
        def k_helper(root, output):
            if root is None:
                return None
            k_helper(root.left, output)
            output.append(root.val)
            k_helper(root.right, output)
        k_helper(root, output)
        return output[k-1]