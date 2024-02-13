"""
User-defined functions and Unittest Lab
Updated By: Carson White
CSCI 110 Lab
Date: 2/8/24

Read and solve - The Last Problem: https://open.kattis.com/problems/thelastproblem

Algorithm:
1. Read the input string using function
3. Create the output as asked and print it using function
3. Test functions using test cases
"""

import sys

def main():
    """Main function that solves the problem.
    """
    data = read_data()
    # FIXED 1: Call answer function passing data as an argument
    # store the returned result into ans variable
    ans = answer(data)
    # FIXED 2: print the result
    print(ans)


def read_data() -> str:
    """Reads the twilight data from std input and returns it.
    Returns:
      str: data read from std input
    """
    # FIXED 3: read and store the input line into data variable
    data = input()
    # FIXED 4: return data
    return data
    pass


def answer(data: str) -> str:
    """Creates the twilight output and returns it.
    Args:
      data (str): name of the person
    Returns:
      str: twilight output
    """
    # FIXED 5: create the output as asked and store it into ans variable
    ans = "Thank you, " + data + " and farewell!"
    return ans


if __name__ == "__main__":
    # FIXME 10: call main function
    main()
    pass