#If you have a text file called "history.txt", do the following separately:
#4- Write a function display_words() in python to read lines from the text file,
# and display those words, which are less than 4 characters
def display_words():

    file = open("history.txt", "r")
    for line in file:
        words = line.split()
        for word in words:
            if len(word) < 4:
                print(word)
    file.close()
    
#5. Write a function in Python to count the words "and" and "or" present in the text file.
# [Note that the words "and" and "or" are complete words]
def count_and_or():
    count_and = 0
    count_or = 0

    file = open("history.txt", "r")
    for line in file:
        words = line.split()
        for word in words:
            if word == "and":
                count_and += 1
            elif word == "or":
                count_or += 1
    file.close()

    print(f'The word "and" appears {count_and} times.')
    print(f'The word "or" appears {count_or} times.')

#6- Write a function in Python to count words in a text file
# those are ending with alphabet "f".
def count_words_ending_with_f():
    count = 0

    file = open("history.txt", "r")
    for line in file:
        words = line.split()
        for word in words:
            if word.endswith('f'):
                count += 1
    file.close()

    print(f'The number of words ending with "f": {count}')

#7- Write a function in Python to count uppercase character in a text file.
def count_uppercase_characters():
    count = 0

    file = open("history.txt", "r")
    for line in file:
        for char in line:
            if char.isupper():
                count += 1
    file.close()

    print(f'The number of uppercase characters: {count}')
