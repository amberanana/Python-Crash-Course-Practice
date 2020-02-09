# 3.1 What is list?
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#3.1.1 Visit the elements from the list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[0].title())

#3.1.2 Index starts from 0
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

#3.1.2 Using value from the list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
