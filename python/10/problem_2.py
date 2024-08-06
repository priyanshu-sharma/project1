class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        start = head
        while start:
            count += 1
            start = start.next
        new_start = head
        count_from_start = count + 1 - n
        new_count = 0
        pre = None
        if count_from_start == 1:
            head = head.next
            return head
        while new_start:
            new_count += 1
            if new_count == count_from_start:
                pre.next = new_start.next
                break
            pre = new_start
            new_start = new_start.next
        return head