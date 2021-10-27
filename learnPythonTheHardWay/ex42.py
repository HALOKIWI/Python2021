## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def hi():
        print("animal says hi")

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
    def hi():
        print("da dawg says hi")
    list=[0,1]
    list2=[0,1,2]

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name
    def hi():
        print("cat says hi")
## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has- a pet of some kind
        self.pet = None
    def hi():
        print("person says hi")

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary
    def hi():
        print("the employee also says hi")

## ??
class Fish(object):
    def yum():
        print("fish is good")

## ??
class Salmon(Fish):

    def hi():
        print("salmon says hi, so many ppl say hi")

## ??
class Halibut(Fish):
    def hi():
        print("the halibut must also say hi")


## rover is- a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()


#1. A class is a user-defined blueprint or prototype from which objects are created. Created because classes provide a means of bundling data and functionality together
#2. yes
#3. ok
#4. found and worked out
#5. ok
#6. yes, multiple inheritance, inherited multiple sources
