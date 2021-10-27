people = 90
cars = 60
buses = 25

# comparing cars and people, if the condition is met, then the stuff behind print will be printed
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")


# comparing buses and cars, print stuff
if buses > cars:
    print("There's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")

#comparing people and buses, print stuff
if people > buses:
    print("Alright, let's just take the buses")
else:
    print("Fine, let's stay home then")


# Study drill 3
if people > cars and people < buses:
    print("I don't know, no idea")
else:
    print("nothing will be printed")

'''
Study Drill 1:
elif is after if, assume that the condition doesn't meet with the first if statement, the code will then compare the condition with the elif statement; else is after elif, assume that the condition doesn't meet with the if and elif statement, then the code will automatically implement the code under the else statement
'''

