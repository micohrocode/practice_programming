# File: sliding_window_solution.py

def length_of_longest_substring(s):
    char_index_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        current_char = s[right]

        if current_char in char_index_map and char_index_map[current_char] >= left:
            left = char_index_map[current_char] + 1  # Move left past last occurrence

        char_index_map[current_char] = right
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
