# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_ptr: ListNode = head
        fast_ptr: ListNode | None = head.next

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        second_head: ListNode = slow_ptr.next
        slow_ptr.next = None
        prev_node: ListNode | None = None

        while second_head:
            next_node: ListNode = second_head.next
            second_head.next = prev_node
            prev_node = second_head
            second_head = next_node

        first_head: ListNode | None = head
        second_head = prev_node

        while second_head:
            temp_first: ListNode | None = first_head.next
            temp_second: ListNode | None = second_head.next
            first_head.next = second_head
            second_head.next = temp_first
            first_head, second_head = temp_first, temp_second            