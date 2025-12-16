#8- A text file named "matter.txt" contains some text,
#  which needs to be displayed such that every next character is separated by a symbol "#"
# . Write a function definition for hash_display() in Python that would display
#  the entire content of the file in the desired format.
def hash_display():
    file = open("matter.txt", "r")
    for line in file:
        modified_line = '#'.join(line.strip())
        print(modified_line)
    file.close()

# 5- write python program to create new file 
#  and write the following 
# lines in it:
# my name is Ahmed
#I have a car and bicycle 
def create_and_write_file():
    file = open("newfile.txt", "w")
    file.write("my name is Ahmed\n")
    file.write("I have a car and bicycle\n")
    file.close()
#6- write Python program to write the "ahmed hussein" to the end of this file:
def append_to_file():
    file = open("newfile.txt", "a")
    file.write("ahmed hussein\n")
    file.close()
#7- write Python program to read the content of one file line by line
#  and store it in another file line by line
def copy_file_content():
    file1 = open("newfile.txt", "r")
    file2 = open("copyfile.txt", "w")
    for line in file1:
        file2.write(line)
    file1.close()
    file2.close()