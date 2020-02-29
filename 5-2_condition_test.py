#5.2 Condition test
#5.2.1
car = 'bmw'
car == 'bmw'

#5.2.2
car = 'Audi'
car ==  'audi'

car = 'Audi'
car.lower() == 'audi'

#5.2.3
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#5.2.4
age = 18
age == 18

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

#5.2.5

    #1 AND
age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >=21

age_1 = 22
age_0 >= 21 and age_1 >=21

(age_0 >=21) and (age_1 >=21)

    #2 OR
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21

age_0 =18
age_0 >= 21 or age_1 >= 21

#5.2.6
requested_topping = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_topping

'pepperoni' in requested_topping

#5.2.7
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
