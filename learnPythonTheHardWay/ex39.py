states = [
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'

]

cities = [
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'

]

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('_' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

print('-' * 10)
for abrev, city in city.items():
    print("%s has the city %s" % (abbrev, city))


print('-' * 10)
for state, abrev in  states.items():
    print("%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)

state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)

#notes: duplicate values override, len(), any data type, type()
#no order

