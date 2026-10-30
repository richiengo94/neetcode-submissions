# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root_deque: deque = deque([root])

        while root_deque:
            curr_node: TreeNode | None = root_deque.popleft()

            if not curr_node:
                continue

            temp_left: TreeNode | None = curr_node.left

            curr_node.left = curr_node.right
            curr_node.right = temp_left

            if curr_node.left:
                root_deque.append(curr_node.left)

            if curr_node.right:
                root_deque.append(curr_node.right)

        return root