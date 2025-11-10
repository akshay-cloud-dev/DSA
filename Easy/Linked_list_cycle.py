class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution():
    def cycle(self, head:ListNode)->bool:
        slow, fast = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

node1 = ListNode(5)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

s = Solution()
print(s.cycle(node1))