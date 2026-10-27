# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head: ListNode = ListNode()
        curr_node: ListNode | None = result_head
        carry: int = 0
        curr_digit: int = 0

        while carry or l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            curr_digit = (carry + l1_val + l2_val) % 10
            carry = (carry + l1_val + l2_val) // 10

            next_node: ListNode = ListNode(curr_digit)

            curr_node.next = next_node
            curr_node = curr_node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return result_head.next