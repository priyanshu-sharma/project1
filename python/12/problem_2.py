class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        start = head
        while start:
            if start.val != 'v':
                start.val = 'v'
                start = start.next
            else:
                return True
        return False