#4.2 Avoid indentation error

#4.2.1. Forget indentation
magicians = ['alice', "david", 'carolina']
for magician in magicians:
 print(magician)

#4.2.2 Forget to zoom the extra code

#4.2.3 Unexpected indent
message = "Hello Python world!"
# print(message)
# There is no need to indent print()

#4.2.5 Forget colon

# Practice
list = ['Hawaiine', 'Margherita', 'Pepperoni']
for pizza in list:
 print(pizza)
 print("I really " + pizza.title() + " pizza!" )
print("I really love pizza.")
print("\n")

# Practice 4-2
animals = ['dog', 'cat', 'rabbit']
for animal in animals:
 print(animal)
 print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")
