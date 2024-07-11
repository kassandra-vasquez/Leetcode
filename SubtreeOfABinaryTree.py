# BRUTE FORCE
# TC: T: O(nm) S: O(h) - h is the height of the root tree
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def recurse(root, subRoot):
            if not root:
                return False
            elif isSameTree(root, subRoot):
                return True
            return recurse(root.right, subRoot) or recurse(root.left, subRoot)
        return recurse(root, subRoot)


# OPTIMIZED
# TC: T: O(nm) - n number of nodes in root, m number of nodes in subRoot S: O(hk) - h height of root, k height of subRoot
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        return False
