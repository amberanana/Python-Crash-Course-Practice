# 3.3 Organizing Lists
#3.3.1 Using sort() to sorting the list permenantly
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse = True)
print(cars)

# 3.3.2 Using sorted() to sort the list temporary
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#3.3.3 Printing the list reversely
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#3.3.4 The length of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
