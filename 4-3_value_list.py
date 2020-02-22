# 4.3 Create value list
# 4.3.1 Using function range()
for value in range(1,5):
 print(value)

for value in range(1,6):
 print(value)

 # 4.3.2 Using range() to create number list
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
 square = value**2
 squares.append(square)

print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# 4.3.3

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min(digits)
max(digits)
sum(digits)

#4.3.4
squares = [value**2 for value in range(1,11)]
print(squares)
