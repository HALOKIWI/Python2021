# create a function which prints stuff
def cheese_and_crackers(cheese_count, boxes_of_crackers): 
    print ("You have %d cheeses:!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers) 
    print ("Man that's enough for a party!")
    print ("Get a blanket.\n")
    print ("We can just give the function numbers directly:")
# own design
def fuck(you):
    for i in range(0,10):
        print(you + i)

# calls the function above, 20 equals to cheese_count, 30 means boxes of crackers
cheese_and_crackers(20, 30)

# print stuff
print ("OR, we can use variables from our script:")

# a variable that equals to 10
amount_of_cheese = 10

# 50 crackers
amount_of_crackers = 50

# calls the function above
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# print stuff
print ("We can even do math inside too:") 

# calls the function
cheese_and_crackers(10 + 20, 5 + 6)

# prints stuff
print ("And we can combine the two, variables and math:")

# calls the function again
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("\n \n")

# own design 10 times
fuck(1)
fuck(2)
fuck(3)
fuck(4)
fuck(5)
fuck(6)
fuck(7)
fuck(8)
fuck(9)
fuck(10)
