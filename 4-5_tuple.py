# 4.5 Tuple

#4.5.1 Defining tuple

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#4.5.2 遍历tuple中所有的值
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#4.5.3 Modify the variable of the tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#Practice
foods = ("apple", "banana", "pineapple", "kiwi", "pear")
for food in foods:
    print(food)

foods = ("apple", "banana", "pineapple", "kiwi", "burger")
for food in foods:
    print(food)
    
#Practic Solution
menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print("- " + item)

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print("- " + item)
