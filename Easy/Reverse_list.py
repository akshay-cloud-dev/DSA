class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solution():
    def reverse(self, head:ListNode)->ListNode:
        prev = None
        cur = head
        while cur:
            var = cur.next
            cur.next = prev
            prev = cur
            cur = var
        return prev

    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
        
    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result


if __name__ == "__main__":
    sl = Solution()
    head1 = sl.create_linked_list([1,2,3,4,5])
    print(sl.linked_list_to_list(head1))
    reversed_head1 = sl.reverse(head1)
    print("Reversed", sl.linked_list_to_list(reversed_head1))
    print()