from sys import argv

script, filename = argv

# print stuff
print("We are going to erase %r" %filename)
print("If you don't want that, hit CTRL-C(^C)")
print("If you do want that. hit Return")

# user will be able to input characters after the question mark
input("?")
print("Opening the file...")

target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n" )

print("And finally, we close it.")
target.close()

txt = open(filename)

print("Here's your file %r: " %filename)

print(txt.read())
print("Type the filename again: ")

file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())



# 4. open file with 'w' will overwrite any existing content in the file
# 5. if we use 'w' then there's no need to include .truncate() in our code
