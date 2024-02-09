"""Test cases for simonsays.py
"""

import simonsays


def test_valid_command():
    """Test valid_command function.
    """
    ans = simonsays.valid_command("Simon says do this")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


def test_valid_command2():
    """Test valid_command function."""
    ans = simonsays.valid_command("do this")
    expected = False
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 7: add a new test case function to test valid_command function
def test_valid_command3():
    """Test valid_command function.
    """
    ans = simonsays.valid_command("Simon says jump up and down")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"


# FIXME 8: add a new test case function to test valid_command function
def test_valid_command4():
    """Test valid_command function.
    """
    ans = simonsays.valid_command("jump up and down")
    expected = True
    assert ans == expected, f"Expected: {expected}, but got: {ans}"



def test_answer():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says do this")
    expected = " do this"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 9: add a new test case function to test answer function

def test_answer():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says don't mix tequilla and vodka")
    expected = " dont mix tequilla and vodka"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"

# FIXME 10: add a new test case function to test answer function

def test_answer():
    """Test answer function.
    """
    ans = simonsays.answer("Simon says touch some grass")
    expected = " touch some grass"
    assert ans == expected, f"Expected: {expected}, but got: {ans}"
