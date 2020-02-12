# 3.3 Organizing Lists
#3.3.1 Using sort() to sorting the list permenantly 使用方法sort() 对列表进行永久性排序
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# 你还可以按与字母顺序相反的顺序排列列表元素，为此，只需向sort() 方法传递参数reverse=True
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
# 注意，调用函数sorted() 后，列表元素的排列顺序并没有变。如果你要按与字母顺序相反的顺序显示列表，也可向函数sorted() 传递参数reverse=True


#3.3.3 Printing the list reversely
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# reverse() 不是指按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序

#3.3.4 The length of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
