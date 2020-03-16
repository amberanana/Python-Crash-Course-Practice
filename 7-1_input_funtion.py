# Chapter 7 User input and while loop
# 7.1 function input()
message = input("Tell me something, and I will reapeat it back to you:")
print(message)

# 7.1.1
name = input("Please enter your name: ")
print("Hello, " + name + "!")

# greeter.py
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

#7.1.2 Using int() to receive number input
age = input("How old are you?")
age = int(age)

# roller_coaster.py
height = input("How tall are you, in inches? ")
height = input(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able ride when you're a little older.")

# 7.1.3 %
# even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + "is even.")
else:
    print("\nThe number " + str(number) + "is odd.")
