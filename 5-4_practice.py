#5-4 Practice

#5-8
username = ['admin', 'adam', 'eve', 'cain', 'abel']

for name in username:
    if name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + name.title() + " , than you for logging in again.")

#5-9
username = []
if username:
    for name in username:
        print("Hello " + name + " , than you for logging in again.")
else:
    print("We need to find some users!")

# 5-10
current_users = ['john', 'andrew', 'bob', 'william', 'fred']
new_users = ['JOHN', 'andrew', 'caroline', 'may', 'anne']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("This username is occupied by someone else in the system.")
    else:
        print("You can use this username to register.")

#5-11
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    else:
        print(str(number) + "th")
