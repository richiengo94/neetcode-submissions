# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_deque: deque = deque([p])
        q_deque: deque = deque([q])

        while p_deque and q_deque:
            p_node: TreeNode = p_deque.popleft()
            q_node: TreeNode = q_deque.popleft()

            if not p_node and not q_node:
                continue

            if (p_node and not q_node) or (not p_node and q_node) or p_node.val != q_node.val:
                return False

            p_deque.append(p_node.left)
            p_deque.append(p_node.right)
            q_deque.append(q_node.left)
            q_deque.append(q_node.right)

        return True