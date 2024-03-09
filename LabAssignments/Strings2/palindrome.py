"""
Lab - Palindrom String Lab - Extra Credit
By: Carson White (5 points)

CSCI 110
Date: 3/7/24 (5 points)

Program prompts user to enter a string and tells whether the given string is palindrome or not.
E.g., mom is a palindrome. Car is not a palindrome.
"""
import sys

def isReversible(phrase):
    # Function to determine whether given phrase is same forward and backward, i.e.,
    # reversible or not.
    length = len(phrase)  # get the length of phrase
    reversible = True  # lets assume every phrase is reversible!
    j = length - 1 # right index
    for i in range(0, length, 1):  # start at 0 end at length-1, step to increment is 1
        # Algorithm steps:
        # 1. go through each character
        #       a. ignore all the non-alphabetic characters on both ends of the phrase
        # 2. compare the corresponding
        #     characters from left and right of the phrase,
        # 3. if a single pair is not equal
        #     the phrase is NOT reversible
        # 4. else, if all the pairs are same, the word is reversible
        if not phrase[i].isalpha():
            continue
        while not phrase[j].isalpha():
            j -= 1
            if j < 0: #if passed the first letter; return False or not reversible
                return True

        #print(i, j, phrase[i], phrase[j])
        if phrase[i] != phrase[j]:
            reversible = False
            break
        j -= 1

    return reversible


def isPalindrome(phrase):
    # Function to determine whether given phrase is palindrome or not
    # Using the following algorithm return True if the phrase is palindrome
    # False otherwise
    # E.g. race car! is a palindrome but jeep is not!
    # Algorithm steps:
    # 1. go through each character up to half of the length of the phrase
    #       a. ignore all the non-alphabetic characters on both ends of the phrase
    # 2. compare the corresponding characters from left and right of the phrase
    # 3. if a single pair do NOT match, phrase is not palindrome, return False
    # 4. else, continue to compare all the corresponding characters and if they all match,
    #       return True
    # FIXME3: Convert the above algorithm to Python code (60 points)
    return True

def test():
    print('running test cases...')
    assert isReversible('race car!') == True
    assert isPalindrome('race car!') == True
    assert isReversible('jeep!') == False
    # FIXME - Fixed uncomment the following line
    assert isPalindrome('jeep!') == False
    assert isReversible('solo!') == False
    print('all test cases passed!')

def main():
    print("Program tells whether the given phrase is reversible and palindrome or not!")

    while True:
        phrase = input("Enter a word or phrase: ")
        # convert the phrase into lowercase
        phrase = phrase.lower()
        if isReversible(phrase):
            print(phrase, " is reversible!")
        else:
            print(phrase, " is not reversible!")

        # FIXME4- Fixed (10 points)
        # Call isPalindrome function and print whether phrase is palindrome or not.
        if isPalindrome(phrase):
            print(phrase, "is a palindrome ")
        else:
            print(phrase, "is not a palindrome")

        # FIXME5-Fixed (20 points)
        # If the user no longer wants to use the program, break the loop!
        # if this is not fixed; program will run infinitely; so enter Ctrl+C to break the loop
        ans = input('Want to continue? [y/n]: ')
        ans = ans.lower()
        #continue of user enters yes or Yes or y or anything that starts with y
        if ans.startswith('y'): 
            continue
        else:
            print('Good bye!')
            break



if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'test':
        test()
    else:
        main()