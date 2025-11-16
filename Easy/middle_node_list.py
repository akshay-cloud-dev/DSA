from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class Solution():
    def Middle_element(self, head:'Optional[ListNode]')->Optional[ListNode]:
        if not head:
            return None
        count =0
        current = head
        while current:
            count+=1
            current = current.next
        mid = count //2

        current = head
        for i in range(mid):
            current = current.next
        return current
    def middleNode(self, head:Optional[ListNode])-> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_from_node(node):
    """Print linked list starting from given node"""
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values

if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Odd length [1,2,3,4,5] -> middle is 3
    head1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = solution.middleNode(head1)
    print(f"Test 1 - List: [1,2,3,4,5]")
    print(f"Middle to end: {print_from_node(middle1)}")  # [3,4,5]
    print()

    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = solution.middleNode(head2)
    print(f"Test 2 - List: [1,2,3,4,5,6]")
    print(f"Middle to end: {print_from_node(middle2)}")  # [4,5,6]
    print()
    
    # Test case 3: Single node [1] -> middle is 1
    head3 = create_linked_list([1])
    middle3 = solution.middleNode(head3)
    print(f"Test 3 - List: [1]")
    print(f"Middle to end: {print_from_node(middle3)}")  # [1]
    print()
    
    # Test case 4: Two nodes [1,2] -> middle is 2
    head4 = create_linked_list([1, 2])
    middle4 = solution.middleNode(head4)
    print(f"Test 4 - List: [1,2]")
    print(f"Middle to end: {print_from_node(middle4)}")  # 