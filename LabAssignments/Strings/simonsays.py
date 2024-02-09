from typing import Union


def main():
    """Main function that solves the problem.
    """
    # step 1. read data
    N = int(input())
    # FIXED 1 - Repeat steps 2-4 N times
    for _ in range(N):   
    # FIXED 2 - read the input string
        command = input()
    # FIXED 3 - call answer function passing the string as an argument
        solution = answer(command)
    # FIXED 4 - print the answer if it returns one, otherwise ignore it
        if solution is not None:
            print(solution)
    


def valid_command(command: str) -> bool:
    """Checks if the string starts with 'Simon says'.

    Args:
        command (str): string to check.

    Returns:
        bool: True if the string starts with 'Simon says', False otherwise.
    """
    # FIXED 5: if the command begins with 'Simon says', return True
    # otherwise, return False
    ans = command.startswith("Simon says")
    return ans


def answer(command: str) -> Union[str, None]:
    """Returns answer given the command or None if the command is not valid.

    Args:
        command (str): string to check

    Returns:
        str|None: rest of the string after 'Simon says' if the command is valid, None otherwise
    """
    valid = valid_command(command)
    # FIXEd 6: if valid is True, return the rest of the string after 'Simon says', None otherwise
    if valid:
        return  command[len("Simon says "):]
    else:
        return None
   


if __name__ == "__main__":
    # call the main function if the script is run from the command line
    main()
