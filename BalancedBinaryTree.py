# TREES

# BRUTE FORCE
# TC: T: O(n log n) S: O(h) - height
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        Lheight = self.getHeight(root.left)
        Rheight = self.getHeight(root.right)

        if abs(Lheight - Rheight) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def getHeight(self, root):
        if not root:
            return 0

        Lheight = self.getHeight(root.left)
        Rheight = self.getHeight(root.right)
        return max(Lheight, Rheight) + 1

# OPTIMIZED
# TC: T&S: O(n)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
