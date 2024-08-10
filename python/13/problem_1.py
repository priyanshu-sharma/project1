class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start1, start2 = list1, list2
        new_head = None
        if not start1:
            return start2
        elif not start2:
            return start1
        else:
            new_head = None
            while start1 and start2:
                if start1.val < start2.val:
                    if new_head is None:
                        new_head = start1
                        new_start = new_head
                    else:
                        new_head.next = start1
                        new_head = new_head.next
                    start1 = start1.next
                elif start1.val > start2.val:
                    if new_head is None:
                        new_head = start2
                        new_start = new_head
                    else:
                        new_head.next = start2
                        new_head = new_head.next
                    start2 = start2.next
                else:
                    if new_head is None:
                        new_head = start1
                        new_start = new_head
                    else:
                        new_head.next = start1
                        new_head = new_head.next
                    start1 = start1.next
                    if new_head is None:
                        new_head = start2
                        new_start = new_head
                    else:
                        new_head.next = start2
                        new_head = new_head.next
                    start2 = start2.next
            if start1:
                if new_head is None:
                    new_head = start1
                    new_start = new_head
                else:
                    new_head.next = start1
                    new_head = new_head.next
            else:
                if new_head is None:
                    new_head = start2
                    new_start = new_head
                else:
                    new_head.next = start2
                    new_head = new_head.next
            return new_start
