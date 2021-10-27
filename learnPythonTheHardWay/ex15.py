# import things
from sys import argv

# unpacked things
script, filename = argv

# open the file (filename will be the name of the file)
txt = open(filename)

# print stuff
print("Here's your file %r: " %filename)

# print what's inside the file
print(txt.read())

# ask the user to type the filename again
print("Type the filename again:")
file_again = input("> ")

# open the file and print what is inside
txt_again = open(file_again)
print(txt_again.read())