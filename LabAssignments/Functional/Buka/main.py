"""
Built-in and Library Functions Lab
Updated By: Carson White
CSCI 110 Lab
Date: 2/6/24

Solution to Kattis problem - Buka: https://open.kattis.com/problems/buka

Algorithm steps:
  1. read the first line or 1st operand into a variable
  3. read the 2nd line or operator into a variable
  3. read the 3rd line or 2nd operand into a variable
  4. concatenate the varialbes into a single string
  5. use the built-in eval function on the concatenated string
  6. print the result of the eval as the answer
"""

import sys

# define a main function


def main():
    """Main function that solves the problem
    """
    # read/input the first operand into A variable using sys library's readline() method
    A = sys.stdin.readline().strip()
    # let's check the value read...
    print(f'{A=}', file=sys.stderr)
    # FIXED - using sys library, read/input the 2nd line into operator variable
    operator = sys.stdin.readline().strip()
    # FIXED - using sys library, read/input the 2nd operand into B variable
    B = sys.stdin.readline().strip()
    # FIXED - concatenate all three variables into a single variable called equation
    equation = B + operator + A
    # call eval(equation) and assign the return value or result into ans variable
    ans = eval(equation)  # FIXME6 - find the answer using eval function
    # print the answer using sys library's stdout.write() method
    sys.stdout.write(f'{ans}\n')


# call main() funtion to execute it
main()