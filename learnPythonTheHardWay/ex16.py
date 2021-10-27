from sys import argv

script, filename = argv

# print stuff
print("We are going to erase %r" %filename)
print("If you don't want that, hit CTRL-C(^C)")
print("If you do want that. hit Return")

# user will be able to input characters after the question mark
input("?")
print("Opening the file...")

# opens the file and overwrite existing content in the file
target = open(filename, 'w')

# truncate means erase all the content in a particular file
print("Truncating the file. Goodbye!")
target.truncate()

# print stuff
print("Now I'm going to ask you for three lines")
# user can input 3 lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# print stuff
print("Now I'm going to write these to the file.")

# write the three lines into the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" )

# print stuff
print("And finally, we close it.")
# close the file
target.close()

# open the file just created
txt = open(filename)

print("Here's your file %r: " %filename)

print(txt.read())
# print stuff
print("Type the filename again: ")

file_again = input(">")
# file_again = input another new name
txt_again = open(file_again)
# read the new file
print(txt_again.read())



# 4. open file with 'w' will overwrite any existing content in the file
# 5. if we use 'w' then there's no need to include .truncate() in our code, cuz 'w' already did the job
