# File: two_pointers_exercise.py

# --- Problem: Pair with Target Sum ---
# Given a sorted array of integers and a target sum, find the indices of the two numbers
# that add up to the target. Return the indices as a list [i, j] (0-based).

# This exercise will use the two pointers technique.

# Function to implement two pointers approach
def pair_with_target_sum(arr, target):
    # Initialize two pointers
    left = 0  # The left pointer starts at the beginning of the array
    right = len(arr) - 1  # The right pointer starts at the end of the array

    # Loop until the two pointers meet
    while left < right:
        # Get the sum of the elements at the left and right pointers
        # (you need to fill this in)
        current_sum = None  # Replace 'None' with the correct expression

        # If the current sum equals the target, return the indices
        if current_sum == target:
            return [left, right]

        # If the current sum is less than the target, we need a bigger number
        # Move the left pointer to the right
        elif current_sum < target:
            # (you need to fill this in)
            pass

        # If the current sum is greater than the target, we need a smaller number
        # Move the right pointer to the left
        else:
            # (you need to fill this in)
            pass

    # If no pair is found, return an empty list
    return []


# --- Test Cases ---
def run_tests():
    # Each test checks if the function returns the correct output

    # Test 1
    arr1 = [1, 2, 3, 4, 6]
    target1 = 6
    print("Test 1 Passed" if pair_with_target_sum(arr1, target1) == [1, 3] else "Test 1 Failed")

    # Test 2
    arr2 = [2, 5, 9, 11]
    target2 = 11
    print("Test 2 Passed" if pair_with_target_sum(arr2, target2) == [0, 2] else "Test 2 Failed")

    # Test 3
    arr3 = [1, 3, 5, 7, 9]
    target3 = 12
    print("Test 3 Passed" if pair_with_target_sum(arr3, target3) == [2, 4] else "Test 3 Failed")

    # Test 4: No valid pair
    arr4 = [1, 2, 3, 9]
    target4 = 8
    print("Test 4 Passed" if pair_with_target_sum(arr4, target4) == [] else "Test 4 Failed")


if __name__ == "__main__":
    run_tests()


# --- Explanation of Key Concepts ---
# 1. This problem assumes the input array is sorted. If it wasn’t, you’d need to sort first (at a cost).
# 2. The two pointers strategy works well here because moving one of the pointers strategically reduces the search space.
# 3. This is much more efficient (O(n)) than checking all pairs (O(n^2)).
# 4. Understanding how to apply this pattern helps with problems involving sorted arrays or linked lists.

# --- Instructions to Student ---
# - Replace the 'None' placeholder with the correct expression to compute the sum of two numbers.
# - Replace the 'pass' statements with the correct pointer movements.
# - Read all comments to understand each step.
# - Run the test cases after filling in the missing parts to validate your solution.
