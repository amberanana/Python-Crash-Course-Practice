#5-3 practice
#5-3 alien color #1

alien_color = 'green'
if alien_color == 'green':
    print("You just received 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just received 5 points!")

#5-4 alien color #2
alien_color = 'green'
if alien_color == 'green':
    print("You just received 5 points!")
else:
    print("You just received 10 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just received 5 points!")
else:
    print("You just received 10 points!")

#5-5 alien color #3
alien_color = 'green'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15
print("You just received " + str(point) + " points.")

alien_color = 'yellow'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15
print("You just received " + str(point) + " points.")

alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15
print("You just received " + str(point) + " points.")

#5-6 Different life stage
age = 17
if age < 2:
    print("He is still a baby.")
elif age < 4:
    print("He's a toddler.")
elif age < 13:
    print("He's a child.")
elif age < 20:
    print("He's a teenager.")
elif age < 65:
    print("He's an adult.")
else:
    print("He is an elder.")

#5-7
favorite_fruits = ['pineapple', 'kiwi', 'watermelon']
if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'blueberry' in favorite_fruits:
    print("You really like blueberry!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapple!")
if 'kiwi' in favorite_fruits:
    print("You really like kiwi!")
if 'watermelon' in favorite_fruits:
    print("You really like watermelon!")
