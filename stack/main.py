# File: stack_based_exercise.py

# --- Problem: Daily Temperatures ---
# Given a list of daily temperatures, return a list where each element is the number of days
# you would have to wait until a warmer temperature. If there is no future day for which this is possible,
# put 0 instead.
#
# Example:
# Input:  [73, 74, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

# This problem requires a stack to keep track of indices of unresolved temperatures.
# You will fill in the missing logic that uses the stack to build the result.

def daily_temperatures(temperatures):
    # The result list is initialized to zeros
    result = [0] * len(temperatures)
    
    # This will hold indices of the temperatures list
    stack = []  # The stack will keep decreasing temperatures indices

    # Loop through the temperatures list
    for current_day, current_temp in enumerate(temperatures):
        # While the stack is not empty and the current temperature is greater than the temperature
        # at the index stored at the top of the stack
        while stack and temperatures[stack[-1]] < current_temp:
            # Pop the index from the stack - this day has now found a warmer day
            prev_day = stack.pop()

            # Calculate the number of days waited and store it in the result
            # (You need to fill this in)
            result[prev_day] = None  # Replace None with the correct calculation

        # Push the current day's index onto the stack
        stack.append(current_day)

    return result


# --- Test Cases ---
def run_tests():
    t1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    print("Test 1 Passed" if daily_temperatures(t1) == expected1 else "Test 1 Failed")

    t2 = [30, 40, 50, 60]
    expected2 = [1, 1, 1, 0]
    print("Test 2 Passed" if daily_temperatures(t2) == expected2 else "Test 2 Failed")

    t3 = [60, 50, 40, 30]
    expected3 = [0, 0, 0, 0]
    print("Test 3 Passed" if daily_temperatures(t3) == expected3 else "Test 3 Failed")

    t4 = [70, 71, 70, 71, 70]
    expected4 = [1, 0, 1, 0, 0]
    print("Test 4 Passed" if daily_temperatures(t4) == expected4 else "Test 4 Failed")

if __name__ == "__main__":
    run_tests()


# --- Explanation of Key Concepts ---
# 1. A monotonic decreasing stack is used to store indices where we haven't yet found a warmer temperature.
# 2. As soon as we find a warmer temperature, we can resolve all prior days on the stack that are colder.
# 3. The difference between the current day and the popped day tells us how many days we waited.

# --- Instructions to Student ---
# - Replace the 'None' with the correct subtraction to calculate the number of days waited.
# - Think about how the stack helps you avoid nested loops (which would be O(n^2)).
# - This solution should run in O(n) time using the stack effectively.
# - Run the test cases to validate your code.
