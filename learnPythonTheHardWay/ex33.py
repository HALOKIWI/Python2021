def loop(num, increment):
    i = 0
    numbers = []

    while i < num:
        print("At the top i is %d" % i)
        numbers.append(i)
        i+=increment
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)


def forLoop(a,b):
    i = 0
    numbers = []

    for i in range(a, b):
        print("At the top i is %d" % i)
        numbers.append(i)
        print("Numbers now: ", numbers)
        print("At the buttom i is %d" %i)



loop(20, 5)

forLoop(0, 13)

'''
study drill 5:
we don't need incrementor in the middle
if we don't get rid of incrementor, then our value of i will be affected

'''



