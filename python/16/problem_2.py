class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        sstart = head
        count = 0
        while start:
            count += 1
            start = start.next
        if count == 1:
            return None
        count = count // 2
        value = 0
        pre = None
        while sstart:
            if value == count:
                if sstart.next is None:
                    pre.next = None
                else:
                    pre.next = sstart.next
            pre = sstart
            sstart = sstart.next
            value += 1
        return head