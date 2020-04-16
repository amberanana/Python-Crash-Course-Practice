# 8.2 Deliver Actual Parameter
# 8.2.1
def describe_pet(animal_type, pet_name):
    "显示宠物的信息"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + "."
          )

describe_pet('hamster', 'harry')

# 1. 调用函数多次
def describe_pet(animal_type, pet_name):
    "显示宠物的信息"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# 2. 位置实参的顺序很重要
def describe_pet(animal_type, pet_name):
    "显示宠物的信息"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')

# 8.2.2 Keyword actual parameter
def describe_pet(animal_type, pet_name):
    "显示宠物信息"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')
# this two functions work same way

# 8.2.3 默认值
def describe_pet(pet_name, animal_type='dog'):
    "显示宠物的信息"
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
# 这个函数只提供了一个实参‘willie’，这个实参将关联到函数定义中的第一个形参pet_name。
# 由于没有给animal_type提供实参，因此Python默认使用其默认值‘dog'

# 注意：使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。
# 这让Python依然能够正确地解读位置实参。

# 8.2.4 等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    # A dog named Willie.
    describe_pet('willie')
    describe_pet(pet_name='willie')

    # A hamster named Harry.
    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')
