#Chapter 5 If statement
#5.1 A simple example
cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
