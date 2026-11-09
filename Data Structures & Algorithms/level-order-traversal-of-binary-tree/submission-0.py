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
        node_deque: deque[TreeNode | None] = deque([root])

        while node_deque:
            temp: list[int] = []
            n_curr_lvl: int = len(node_deque)

            for i in range(n_curr_lvl):
                curr_node: TreeNode | None = node_deque.popleft()
                
                if curr_node:
                    temp.append(curr_node.val)
                    node_deque.append(curr_node.left)
                    node_deque.append(curr_node.right)

            if temp:
                result.append(temp)

        return result