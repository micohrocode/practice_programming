# File: linked_list_solution.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0  # Use 0 if l1 is None
        val2 = l2.val if l2 else 0  # Use 0 if l2 is None

        total = val1 + val2 + carry
        carry = total // 10  # Get new carry
        current.next = ListNode(total % 10)  # Create new node with digit
        current = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy_head.next


# --- Helper Functions for Testing ---

def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# --- Test Cases ---

def run_tests():
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = add_two_numbers(l1, l2)
    print("Test 1 Passed" if linked_list_to_list(result) == [7, 0, 8] else "Test 1 Failed")

    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = add_two_numbers(l1, l2)
    print("Test 2 Passed" if linked_list_to_list(result) == [0] else "Test 2 Failed")

    l1 = list_to_linked_list([9,9,9,9,9,9,9])
    l2 = list_to_linked_list([9,9,9,9])
    result = add_two_numbers(l1, l2)
    print("Test 3 Passed" if linked_list_to_list(result) == [8,9,9,9,0,0,0,1] else "Test 3 Failed")

if __name__ == "__main__":
    run_tests()
