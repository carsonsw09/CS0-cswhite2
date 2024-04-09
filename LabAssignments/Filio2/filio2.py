"""
File I/O Lab with Dictionary

Update By: Carson White

CSCI 110
Date: 4/3/2024

Program finds the frequency of words in a given text document and print top 10 most
common words using dictionary and tuple data structures.
"""


def readText():
    """
    opens a file reads its contnets and
    creates a histogram of words based on frequency using dictionary data structure
    """
    fileOk = False
    fin = None
    hist = {}
    # stores data in this form: hist = {'and': 10, 'python':15}
    # where 'and' appears 10 times and
    # python appears 15 times

    while not fileOk:
        fileName = input('Enter input text file => ')
        try:
            fin = open(fileName, 'r')
            fileOk = True
        except Exception as ex:
            print('Exception occured: ', ex)

    lines = fin.readlines()
    for line in lines:
        line = line.strip().lower()
        if line:
            # FIXME3- Fixed
            # update words; split line into list of words and store the list into words object
            words = line.split()
            for word in words:
                # FIXME4- Fixed
                # if word exists as key in hist dict, increment the value by 1
                # else add word as new key with value 1 in hist dict
                if word in hist:
                    hist[word] += 1
                else:
                    hist[word] = 1
                
                
    return hist


def reverseHistogramList(histDict):
    """
    given someDict,  returns list of tuples in descending order based 
    frequency of each word in histDict
    """
    reverseList = []
    for key, val in histDict.items():
        # FIXME5-Fixed
        # append tuple with values in (val, key) order into reverseList list
        reverseList = [(val, key) for key, val in histDict.items()]

    # FIXME6- Fixed
    # Sort the list reverseList in reverse order
    reverseList.sort(reverse=True)
    return reverseList
    


def main():
    histogram = readText()
    # FIXME7-Fixed - Comment the following statement out when done
    ##print(histogram)  # see the output to understand what's going on so far

    aList = reverseHistogramList(histogram)
    # FIXME8- Fixed – print top 10 words with highest frequencies stored in aList
    print(" The top 10 words with the highest frequencies stored in the a list are,  ")
    for freq in aList[:10]:
        print(f"Word: {freq[1]} ")


if __name__ == "__main__":
    main()