# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result: list[list[int]] = []
        
        def dfs(curr_node: TreeNode | None, curr_depth: int) -> None:

            nonlocal result

            if not curr_node:
                return

            if curr_depth > len(result):
                result.append([])
            
            result[curr_depth - 1].append(curr_node.val)
            dfs(curr_node.left, curr_depth + 1)
            dfs(curr_node.right, curr_depth + 1)

        dfs(root, 1)

        return result