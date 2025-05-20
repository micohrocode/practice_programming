# File: stack_based_solution.py

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for current_day, current_temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < current_temp:
            prev_day = stack.pop()
            result[prev_day] = current_day - prev_day  # Correct: wait time calculation

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
