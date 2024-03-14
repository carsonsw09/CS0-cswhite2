def decode(text_link):
    # Step 1: Read the file and parse each line
    number_word_map = {}
    with open(text_link, 'r') as file:
        for line in file:
            number, word = line.split()
            number_word_map[int(number)] = word
    
    # Step 2: Determine the necessary numbers and extract words
    words = []
    n = 1
    while True:
        # Calculate the triangular number for the current row
        triangular_number = n * (n + 1) // 2
        if triangular_number in number_word_map:
            words.append(number_word_map[triangular_number])
            n += 1
        else:
            break
    
    # Step 3: Combine words to form the message
    message = ' '.join(words)
    return message

# Example usage:
# Assuming you've saved the provided example in a file named 'encoded_message.txt'
text_link = r'C:\Users\carso\110\CS0-cswhite2\LabAssignments\Strings\coding_qual_input.txt'
message = decode(text_link)
print(message)

