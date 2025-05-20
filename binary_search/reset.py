# File: binary_search_exercise.py

# --- Problem: Find First and Last Position of Element in Sorted Array ---
# Given an array of integers nums sorted in non-decreasing order, find the starting
# and ending position of a given target value.
# If the target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3, 4]

# This problem requires two binary searches: one to find the first position,
# and one to find the last position of the target.

def find_first_and_last(nums, target):
    # Helper function to find the left boundary (first occurrence)
    def find_left():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid  # potential result found
                # Now move the search to the left half
                # (you need to fill this in)
                right = None  # replace None with the correct expression
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    # Helper function to find the right boundary (last occurrence)
    def find_right():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                # Now move the search to the right half
                # (you need to fill this in)
                left = None  # replace None with the correct expression
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    # Final result is a list of first and last positions
    return [find_left(), find_right()]


# --- Test Cases ---
def run_tests():
    nums1 = [5,7,7,8,8,10]
    target1 = 8
    expected1 = [3, 4]
    print("Test 1 Passed" if find_first_and_last(nums1, target1) == expected1 else "Test 1 Failed")

    nums2 = [5,7,7,8,8,10]
    target2 = 6
    expected2 = [-1, -1]
    print("Test 2 Passed" if find_first_and_last(nums2, target2) == expected2 else "Test 2 Failed")

    nums3 = []
    target3 = 0
    expected3 = [-1, -1]
    print("Test 3 Passed" if find_first_and_last(nums3, target3) == expected3 else "Test 3 Failed")

    nums4 = [1]
    target4 = 1
    expected4 = [0, 0]
    print("Test 4 Passed" if find_first_and_last(nums4, target4) == expected4 else "Test 4 Failed")

    nums5 = [2, 2, 2, 2, 2]
    target5 = 2
    expected5 = [0, 4]
    print("Test 5 Passed" if find_first_and_last(nums5, target5) == expected5 else "Test 5 Failed")

if __name__ == "__main__":
    run_tests()


# --- Explanation of Key Concepts ---
# 1. Binary search is used twice: once to find the first index, once to find the last.
# 2. In each case, when we find the target, we do NOT return immediately.
#    Instead, we continue the search in one direction to find the boundary.
# 3. The time complexity remains O(log n) because each binary search still discards half the search space each time.

# --- Instructions to Student ---
# - Replace the 'None' values with correct logic to move left or right accordingly.
# - Understand how the helper functions are specialized for left and right boundaries.
# - Run the test cases to verify your solution works correctly across edge cases.
