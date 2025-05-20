# File: linked_list_exercise.py

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1, l2):
    # Create a dummy head to simplify result list creation
    dummy_head = ListNode(0)

    # Pointer to build the result list
    current = dummy_head

    # Keep track of carry from the previous digit addition
    carry = 0

    # Loop while there are still nodes to process in either list or a leftover carry
    while l1 or l2 or carry:
        # Extract the current values from l1 and l2
        # If a list is already done, treat its value as 0
        val1 = ___  # FILL IN: Use l1.val if l1 is not None, else 0
        val2 = ___  # FILL IN: Use l2.val if l2 is not None, else 0

        # Add the digits along with any carry
        total = ___  # FILL IN: Sum val1 + val2 + carry

        # Update carry for next iteration
        carry = ___  # FILL IN: Integer division of total by 10

        # Create a new node with the digit (total % 10)
        current.next = ___  # FILL IN: Create a ListNode with total % 10
        current = current.next

        # Move to the next node in l1 and l2 if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Return the result, skipping the dummy head
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
