#6-3 Practice
#6-4 vocab list_solution

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)

#6-5 Rivers
rivers = {
    'Nile': 'Egpyt',
    'Yangtze River': 'China',
    'Yellow River': 'China',
    'Danube': 'Europe',
    }
for river, place in rivers.items():
    print(("\n") + "The " + river + " runs through " + place)

for river in rivers.keys():
    print(river)

for place in rivers.values():
    print(place)

# 6-6 poll
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
name_list = ['jen', 'sarah', 'edward', 'phil', 'erin', 'john']

for name in name_list:
    if name in favorite_languages.keys():
        print(name.title() + ", thank you for taking your poll!")
    else:
        print(name.title() + ", please take the poll!")
