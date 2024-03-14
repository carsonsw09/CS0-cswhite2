"""
Lists and Unittest Lab
Updated By: Carson White
CSCI 110 Lab
Date: 3/14/24

Read and solve - Pet: https://open.kattis.com/problems/pet 

Algorithm steps:
    1. Create a list to store the total scores of each contestant
    2. Repeat 5 times:
        i. Read the input line
        ii. Split the line into a list of numbers
        iii. Convert the list of strings into a list of ints
        iv. Sum the list of ints
        v. Append the sum to the list of scores
    3. Find the max score in the list of scores
    4. Find the index of the max score in the list of scores
    5. Print the index of the max score + 1 and the max score
"""


from typing import List


def main() -> None:
    """Main function that solves the problem
    """
    # step 1. create a list to store the total scores of each contestant
    scores = []
    # FIXME-Fixed 1 - repeat step 2-4 5 times
    # FIXME-Fixed 2 - read the input line as a list of integers using get_data function
    # FIXME-Fixed 3 - find the sum of scores using list_sum function
    # FIXME-Fixed 4 - append the sum to the list of scores
    # FIXME-Fixed 5 - print the final output calling answer function
    for i in range(5):
        data_scores = get_data()
        sum_scores = list_sum(data_scores)
        scores.append(sum_scores)
    
    print(answer(scores))
    test_answer()
    


def get_data() -> List[int]:
    """Reads the data from std input and returns it as a list of ints
    Args:
        None
    Returns:
        List[int]: list of ints
    """
    str_nums = input().split()  # list of string numbers
    # FIXME-Fixed 6: convert str_nums as list of ints and return it
    int_list = [int(num) for num in str_nums]
    return int_list 


def list_sum(numbers: List[int]) -> int:
    """Finds and returns sum of the numbers in the list.
    Args:
        numbers: List[int]: # takes a list of numbers as a parameter

    Returns:
        int: sum of the numbers in the list
    """
    # FIXME-Fixed 7: find the sum of the numbers in the list and return it
    ans = sum(numbers)
    return ans


def answer(scores: List[int]) -> str:
    """Find and return the answer as a string.
    Args:
        scores (List[int]): List of 5 contestants scores
    Returns:
        str: index of the max score + 1 and the max score as a string
    """
    max_score = max(scores)
    index = scores.index(max_score)
    # FIXME-Fixed 8: return the index+1 and the max number in the list as a string
    return f"{index+1} {max_score}"

def test_answer():
    print("Testing the answer function... ")
    
    scores = [10,20,30,40,50]
    expected ="5 50"
    test_ans = answer(scores)
    assert test_ans == expected, f"Test case failed. 2: Expected{expected}, got{test_ans}"
    
    scores = [12,9,15,9,3]
    expected ="3 15"
    test_ans = answer(scores)
    assert test_ans == expected,  f"Test case failed. 2: Expected{expected}, got{test_ans}"
    
    scores = [100,101,101,102, 5]
    expected ="4 102"
    test_ans = answer(scores)
    assert test_ans == expected,  f"Test case failed. 2: Expected{expected}, got{test_ans}"
    
    print("All test-cases passed succesfully, this program operates within the parameters")


if __name__ == "__main__":
    main()