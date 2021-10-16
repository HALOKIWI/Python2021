name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("Let's talk about %s." % name)
print("He's %d inches tall." % height)
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (eyes, hair))
print(f"His teeth are usually {teeth} depending on the coffee.")
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")



def convertInchToCm(num):
    num*=2.54
    return num

def convertPoundsToKilos(num):
    num*=0.453592
    return num


convertedNum = convertInchToCm(7)
print(convertedNum)

convertedNum2 = convertPoundsToKilos(2000)
print(convertedNum2)