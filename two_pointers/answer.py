# File: two_pointers_solution.py

def pair_with_target_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]  # Correct: Sum of elements at the pointers

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1  # Move left pointer to the right to increase the sum
        else:
            right -= 1  # Move right pointer to the left to decrease the sum

    return []

# --- Test Cases ---
def run_tests():
    arr1 = [1, 2, 3, 4, 6]
    target1 = 6
    print("Test 1 Passed" if pair_with_target_sum(arr1, target1) == [1, 3] else "Test 1 Failed")

    arr2 = [2, 5, 9, 11]
    target2 = 11
    print("Test 2 Passed" if pair_with_target_sum(arr2, target2) == [0, 2] else "Test 2 Failed")

    arr3 = [1, 3, 5, 7, 9]
    target3 = 12
    print("Test 3 Passed" if pair_with_target_sum(arr3, target3) == [2, 4] else "Test 3 Failed")

    arr4 = [1, 2, 3, 9]
    target4 = 8
    print("Test 4 Passed" if pair_with_target_sum(arr4, target4) == [] else "Test 4 Failed")

if __name__ == "__main__":
    run_tests()
