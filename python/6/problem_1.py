class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        while head:
            new_node = ListNode(head.val)
            if start is None:
                start = new_node
            else:
                new_node.next = start
                start = new_node
            head = head.next
        return start