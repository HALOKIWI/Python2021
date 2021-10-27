def add(a, b):
    print("ADDING %d + %d" %(a,b))
    return a + b


def subtract(a, b):
    print("SUBTRACTING %d - %d" %(a,b))
    return a - b


def multiply(a, b):
    print("Multiplying %d * %d" %(a,b))
    return a * b


def divide(a, b):
    print("DIVIDING %d / %d" %(a,b))
    return a / b


print("Let's do some math with just functions")

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)


print("Age: %d, Height: %d, Weight: %d, IQ: %d" %(age, height, weight, iq))

print("Here is a puzzle")

puzzle = add(age, subtract(height, multiply(weight, divide(iq, 2))))

# drill 2 and drill 3

num1 = divide(200,2)
num2 = multiply(weight, num1)
num3 = subtract(20435, num2)
num4 = add(age, num3)

print("That becomes: ", puzzle, " can you do it by hand")

print("Answer through normal formula: ", num4)

# study drill 1

def test(i, j):
    return i+j+j+i

num = test(2, 4);
print(num)



# study drill 4

puzzle1 = multiply(height, add(iq, subtract(weight, age)))
print("drill 4: calculate by myself --- ", puzzle1)



