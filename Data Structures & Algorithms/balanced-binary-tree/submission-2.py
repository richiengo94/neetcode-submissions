# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]) -> list[int, bool]:

            if root is None:
                return [0, True]
            
            h_left, bal_left = dfs(root.left)
            h_right, bal_right = dfs(root.right)

            return [1 + max(h_left, h_right), bal_left and bal_right and abs(h_left - h_right) <= 1]

        return dfs(root)[1]