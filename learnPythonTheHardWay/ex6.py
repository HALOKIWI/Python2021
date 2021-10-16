types_of_people = 10
x = f"There are {types_of_people} types of people." # string inside string
# there are 10 types of people
# f"" is similar to str.format
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}." # string is put inside string

# print x and y
print(x)
print(y)

# print the following sentences (formated)
print(f"I said: {x}") # sting is put inside string
print(f"I also said: '{y}'") # string is put inside string

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
# add two strings together