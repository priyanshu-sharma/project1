class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = new_start = None
        start = head
        start = start.next
        value = 0
        while start:
            if start.val == 0:
                new_node = ListNode(val=value)
                if new_start is None:
                    new_start = new_node
                    new_head = new_start
                else:
                    new_start.next = new_node
                    new_start = new_start.next
                value = 0
            value += start.val
            start = start.next
        return new_head