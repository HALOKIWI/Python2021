ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

# insert every word in ten_things into stuff
stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# this is a while loop to make sure that stuff gains 10 things
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one) # add next_one into stuff
    print("There's %d items now" %len(stuff))

#print every single thing in stuff
print("There we go: ", stuff)
print("Let's do some things with stuff")

# print the second thing in stuff
print(stuff[1])
# print the last thing in stuff
print(stuff[-1])
# pop starts from the end of a list; moreover, it will also return the value being poped
print(stuff.pop())
# insert space between every 2 things
print(' '.join(stuff))
# replace the fourth one with #
print('#'.join(stuff[3:5])) 


'''
Study Drill 5
dir is an inbuilt function which literally produces a list of all of the attributes on a specific object (be that a class, or an instance).

The ‘class’ of an object is (for want of a better analogy) the ‘tenplate’ that is used to build that object.
'''
