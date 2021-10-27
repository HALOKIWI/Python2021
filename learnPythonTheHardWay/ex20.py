from sys import argv

script, input_file = argv

# this is the function that prints all the lines in the file
def print_all(f):
    print(f.read())

# rewind is a function that includes file seek, and file seek is a method that sets the file's position
def rewind(f):
    f.seek(0)

# this is a function that prints out the current line number and prints out the according line
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open file through new variable called current_file
current_file = open(input_file)

# print stuff
print("First let's print the whole file:\n")

# call the printall function to print out all the lines in the file
print_all(current_file)

# print stuff
print("Now let's rewind, kind of like a tape.")

# calls the rewind function and move the current position
rewind(current_file)

# print stuff
print("Let's print three lines.")

# set current_line to 1
current_line = 1

# print out the first line
print_a_line(current_line, current_file)

# add 1 to current_line
current_line+=1

# print out the second line
print_a_line(current_line, current_file)

# add 1 to current line
current_line+=1

# print out the third line
print_a_line(current_line, current_file)


# x+=1  means  x = x + 1
