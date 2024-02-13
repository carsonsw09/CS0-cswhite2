"""Module to test functions from main.py
"""

import sys
import main

# test function must start with test_ prefix for pytest to recognize it


def test_answer():
    """Test answer function
    """
    ans = main.answer("Alice")
    expected = "Thank you, Alice, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    ans = main.answer("Bob")
    expected = "Thank you, Bob, and farewell!"  # FIXMED: fix the expected output
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    # FIXED 6: add a new test case to test your answer function
    ans = main.answer("John")
    expected = "Thank you, John, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    # FIXED 7: add a new test case to test your answer function
    ans = main.answer("Micheal")
    expected = "Thank you, Micheal, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    # FIXED 8: add a new test case to test your answer function
    ans = main.answer("Henry")
    expected = "Thank you, Henry, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    # FIXED 9: add a new test case to test your answer function
    ans = main.answer("Bob")
    expected = "Thank you, Bob, and farewell!"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
    print("All test cases passed...", file=sys.stderr)


if __name__ == "__main__":
    test_answer()