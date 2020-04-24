#Practice 8.5
# 8-12 Sandwich
def make_sandwich(*toppings):
    "概述三明治制作所需的材料"
    print("\nMaking a sandwich with following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sandwich('mushroom', 'ham', 'black olives')
make_sandwich('green pepper', 'chicken breast', 'tomato slices')
make_sandwich('roasted beef', 'lettuce', 'cucumber')

# 8-13 User info
def build_profile(first, last, **user_info):
    "创建一个字典，其中包含我们知道的有关用户的一切"
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Amber', 'Lou',
                             location = 'hangzhou',
                             field = 'international affairs')
print(user_profile)
user_profile = build_profile('Alex', 'Johnson',
                             location = 'lancaster',
                             field = 'math')
print(user_profile)
user_profile = build_profile('Maria', 'Wood',
                             location = 'new haven',
                             field = 'comparative literature')
print(user_profile)

# 8-14 Automobile
def make_car(manufacturer, model, **other_info):
    "创建字典，包括有关车的一切信息"
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in other_info.items():
        profile[key ] = value
    return profile

auto_info = make_car('subaru', 'outback', color = 'blue', two_package = True)
print(auto_info)
auto_info = make_car('bmw', 'q7', color = 'silver')
print(auto_info)
auto_info = make_car('benz', 'g550', color = 'red', four_by_four = True)
print(auto_info)
