# File: sliding_window_exercise.py

# --- Problem: Longest Substring Without Repeating Characters ---
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# This problem requires the sliding window technique to maintain a window of unique characters.
# You will use a set or dictionary to track seen characters and adjust the window when duplicates are found.

def length_of_longest_substring(s):
    # Dictionary to store the last index of each character
    char_index_map = {}

    # Initialize window pointers and max length
    left = 0  # Start of the sliding window
    max_length = 0

    # Iterate over characters in the string
    for right in range(len(s)):
        current_char = s[right]

        # If the character is already in the window (and its index is within bounds)
        if current_char in char_index_map and char_index_map[current_char] >= left:
            # Move the left side of the window right after the last occurrence of current_char
            left = None  # Replace None with the correct update

        # Update the last seen index of the character
        char_index_map[current_char] = right

        # Update the max length of the window
        max_length = max(max_length, right - left + 1)

    return max_length


# --- Test Cases ---
def run_tests():
    print("Test 1 Passed" if length_of_longest_substring("abcabcbb") == 3 else "Test 1 Failed")
    print("Test 2 Passed" if length_of_longest_substring("bbbbb") == 1 else "Test 2 Failed")
    print("Test 3 Passed" if length_of_longest_substring("pwwkew") == 3 else "Test 3 Failed")
    print("Test 4 Passed" if length_of_longest_substring("") == 0 else "Test 4 Failed")
    print("Test 5 Passed" if length_of_longest_substring("dvdf") == 3 else "Test 5 Failed")

if __name__ == "__main__":
    run_tests()


# --- Explanation of Key Concepts ---
# 1. A sliding window [left, right] maintains the current substring with all unique characters.
# 2. If a character is repeated, the left pointer is moved to one position after its last occurrence.
# 3. The dictionary helps in constant-time lookup and window updates.
#
# --- Instructions to Student ---
# - Replace 'None' with the correct logic to update the left pointer when duplicates are found.
# - Understand how the sliding window adapts as you traverse the string.
# - Run all test cases to confirm the function behaves correctly.