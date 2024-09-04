class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = None
        new_head = None
        carry = 0
        while l1 or l2 or carry:
            value = 0
            if carry > 0:
                value += carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            if value > 9:
                iv = value % 10
                carry = value // 10
            else:
                iv = value
                carry = 0
            
            new_node = ListNode(val=iv)
            if start is None:
                start = new_node
                new_head = start
            else:
                start.next = new_node
                start = start.next
        return new_head