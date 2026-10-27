# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result: ListNode | None = ListNode(next=head)

        curr_node: ListNode | None = result
        lead_node: ListNode | None = head

        for i in range(n):
            lead_node = lead_node.next

        while lead_node:
            lead_node = lead_node.next
            curr_node = curr_node.next
        
        curr_node.next = curr_node.next.next

        return result.next
