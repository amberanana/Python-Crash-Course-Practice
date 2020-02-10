# 3.2.1 Modifying the elements from the list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# 3.2.2 Adding elements
#3.2.2.1 Adding elements at the end of the list
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles.append("ducati")
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# 3.2.2.2 Inserting elements into the list
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.insert(0, 'ducati')
print(motorcycles)

#3.2.3 Deleting the elements
#3.2.3.1 Using del sentence to delete the elements
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#3.2.3.2 Using method pop() to delete elements
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#3.2.3.3 Pop the elements from anywhere in the list
motorcycles = ["honda", "yamaha", "suzuki"]
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#3.2.3.4 Using value to delete elements
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")
