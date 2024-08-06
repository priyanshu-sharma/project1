class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        
        if p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot is None:
            return True
        if root is None and subRoot:
            return False
        if root and subRoot:
            return (self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
        return False        