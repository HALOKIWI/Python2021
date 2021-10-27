the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" %number)


for fruit in fruits:
    print("A fruit of type: %s" % fruit)

for i in change:
    print("I got %r" % i)

elements = []

for i in range(0,6):
    print("Adding %d to the list." % i)
    elements.append(i)

for i in elements:
    print("Element was: %d" % i)


# study drill 2: yes
'''
Study Drill 3:

append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''
