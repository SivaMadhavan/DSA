class Solution:
    @staticmethod
    def reverse_list(head):
        prev, current = None, head
        if not head:
            return None
        while current:
            _next = current.next
            current.next = prev
            prev = current
            current = _next
        return prev
