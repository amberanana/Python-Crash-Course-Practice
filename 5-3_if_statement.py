#5.3 If statement
#5.3.1
# if conditional_test:
#   do something

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#5.3.2 if-else sentence
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else structure
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

#5.4. Using multi elif
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price =10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

#5.3.5 ignore else
#Python does not require if-elif structure follow with else
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

#5.3.6
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
