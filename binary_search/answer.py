# File: binary_search_solution.py

def find_first_and_last(nums, target):
    def find_left():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                right = mid - 1  # Move left to find first occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

    def find_right():
        left, right = 0, len(nums) - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                left = mid + 1  # Move right to find last occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

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
